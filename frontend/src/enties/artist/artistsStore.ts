
import { create } from 'zustand';
import { BASE_URL } from '../../shared/api/client';

export type Artist = {
  public_id: string,
  name: string,
  genres: { id: number, name: string }[],
  avatar?: string | null
}

type ArtistStore = {
  artists: Artist[],
  isLoading: boolean,
  error: string | null,
  fetchArtists: () => Promise<void>
}

export const useArtistStore = create<ArtistStore>((set) => ({
  artists: [],
  isLoading: false,
  error: null,
  fetchArtists: async () => {
    set({ isLoading: true, error: null });

    try {
      const response = await fetch(`${BASE_URL}/music/artists/`)
      if (!response.ok) {
        throw new Error('Can`t find. 404')
      }

      const data = await response.json();
      set({ artists: data });

    } catch (err) {
      set({error: err instanceof Error ? err.message : 'Loading error...'})
    } finally {
      set({isLoading: false})
    }

      }
}));
