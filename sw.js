// Shmung Machine service worker: no offline caching. Clears any caches left by older versions
// so the newest deploy always loads.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(
  caches.keys().then(keys => Promise.all(keys.map(k => caches.delete(k)))).then(() => self.clients.claim())
));
