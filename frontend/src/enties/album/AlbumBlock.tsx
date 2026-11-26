import { useEffect } from 'react';
import { useAlbumStore } from './albumStore';

export function Albums() {
  const { albums, fetchAlbum } = useAlbumStore();

  useEffect(() => {
    fetchAlbum()
  }, [fetchAlbum])

  const listAlbums = albums.slice(0, 4).map(album => <li key={album.public_id} className="artist-card">
    <a href={`#artist-${album.public_id}`} className="artist-link" onClick={(e) => { e.preventDefault(); console.log('You clicked the artist:', album.title, album.public_id) }}>
      {album.cover ? (
        <img src={album.cover} alt={album.title} className="artist-avatar" />
      ) : (
        <div className="artist-avatar-placeholder">{album.title[0]}</div>
      )}

      <p className="artist-name">{album.title}</p>
    </a>
  </li>)

  return (
    <>
      <section id="albums" className="artists-section">
        <h2 className="artists-title">Popular Albums</h2>
      <ul className="artists-list">{listAlbums}</ul>
      </section>
    </>
  )
}
