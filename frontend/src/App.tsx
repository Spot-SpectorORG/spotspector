
import { useEffect, useState } from 'react'

type Track = {
  id: number,
  title: string,
  artists: { id: number; name: string }[],
  duration: string
}

export default function App() {
  const [tracks, setTracks] = useState<Track[]>([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/v1/music/tracks/').then((res) => {
      if (!res.ok) throw new Error(`Error ${res.status}`)
      return res.json()
    })
      .then(setTracks)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  return (
    <>
      <h1>SpotSpector</h1>
      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}
      {!loading && !error && tracks.length === 0 && <p>There is no tracks yet :(</p>}

      <ul>
        {tracks.map((t) => (
          <li key={t.id}>
            {t.title}, {t.artists.map((a) => a.name).join(', ')} ({t.duration})
          </li>
        ))}
      </ul>
    </>
  )
}
