import { create } from 'zustand';
import { BASE_URL } from '../../shared/api/client';


type Album = {
  public_id: string,
  title: string,
  artists: { public_id: string, name: string }[],
  cover: string | null,
  release_date: string,
}

type AlbumStore = {
  albums: Album[],
  isLoading: boolean,
  error: string | null,
  fetchAlbum: () => Promise<void>,
}

export const useAlbumStore = create<AlbumStore>((set) => ({
  albums: [],
  isLoading: false,
  error: null,
  fetchAlbum: async () => {
    set({ isLoading: true, error: null });

    try {
      const res = await fetch(`${BASE_URL}/music/albums/`);

      if (!res.ok) {
        throw new Error('Can`t find. 404')
      }

      const data = await res.json()
      set({ albums: data })

    } catch (err){
      set({error:  err instanceof Error ? err.message : 'Loading Error'})
    } finally {
      set({isLoading: false})
    }

  }
}))
