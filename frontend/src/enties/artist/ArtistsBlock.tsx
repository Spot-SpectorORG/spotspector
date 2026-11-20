import { useEffect } from 'react';
import { useArtistStore } from './artistsStore';

export function Artists() {
  const { artists, isLoading, error, fetchArtists } = useArtistStore();

  useEffect(() => {
    fetchArtists()
  }, [fetchArtists])


  if (isLoading) {
    return <div>Loading...</div>
  }
  if (error) {
    return <div>Error</div>
  }

  const listArtists = artists.slice(0, 6).map(artist => <li key={artist.public_id} className="artist-card">
    <a href={`#artist-${artist.public_id}`} className="artist-link" onClick={(e) => { e.preventDefault(); console.log('You clicked the artist:', artist.name, artist.public_id) }}>
      {artist.avatar ? (
        <img src={artist.avatar} alt={artist.name} className="artist-avatar" />
      ) : (
        <div className="artist-avatar-placeholder">{artist.name[0]}</div>
      )}

      <p className="artist-name">{artist.name}</p>
    </a>
  </li>)

  return (
    <>
      <section className="artists-section">
        <h2 className="artists-title">Popular Artists</h2>
      <ul className="artists-list">{listArtists}</ul>
      </section>
    </>
  )
}
