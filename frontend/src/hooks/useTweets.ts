import { useState, useEffect, useCallback } from "react";
import api from "../services/api";
import { useAuth } from "./useAuth";

export interface CommentType {
  id: number;
  author_email: string;
  content: string;
  created_at: string;
}

export interface TweetType {
  id: number;
  username: string;
  user_id: number;
  author_id: number;
  content: string;
  timestamp: string;
  likes_count: number;
  replies_count: number;
  comments: CommentType[];
  is_following: boolean;
  handle?: string;
  liked_by_me: boolean;
  retweets_count: number;
}

export function useTweets() {
  const [tweets, setTweets] = useState<TweetType[]>([]);
  const [loading, setLoading] = useState(false);
  const { isAuthenticated } = useAuth();

  const fetchTweets = useCallback(async () => {
    if (!isAuthenticated) return;

    try {
      setLoading(true);
      const response = await api.get<TweetType[]>("/api/tweets/");
      setTweets
