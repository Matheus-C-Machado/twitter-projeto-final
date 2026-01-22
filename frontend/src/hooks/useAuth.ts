import { create } from "zustand";
import api from "../services/api";

interface AuthState {
  isAuthenticated: boolean;
  token: string | null;
  login: (email: string, password: string) => Promise<void>;
  signup: (
    email: string,
    password: string,
    passwordConfirmation: string
  ) => Promise<void>;
  logout: () => void;
  restoreSession: () => void;
}

export const useAuth = create<AuthState>((set) => ({
  isAuthenticated: false,
  token: localStorage.getItem("access_token"),

  login: async (email, password) => {
    try {
      const response = await api.post("/api/users/token/", {
        email,
        password,
      });

      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);

      set({
        isAuthenticated: true,
        token: response.data.access,
      });
    } catch (error) {
      console.error("Erro no login:", error);
      set({ isAuthenticated: false, token: null });
      throw error;
    }
  },

  signup: async (email, password, passwordConfirmation) => {
    try {
      await api.post("/api/users/signup/", {
        email,
        password,
        password_confirmation: passwordConfirmation,
      });

      // login automático após cadastro
      await useAuth.getState().login(email, password);
    } catch (error) {
      console.error("Erro no signup:", error);
      throw error;
    }
  },

  logout: () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");

    set({ isAuthenticated: false, token: null });
    window.location.href = "/login";
  },

  restoreSession: () => {
    const token = localStorage.getItem("access_token");

    if (token) {
      set({ isAuthenticated: true, token });
    } else {
      set({ isAuthenticated: false, token: null });
    }
  },
}));
