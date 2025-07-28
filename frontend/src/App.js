import React, { useEffect, useState } from 'react';

function App() {
  const [msg, setMsg] = useState('Loading...');

  useEffect(() => {
    fetch("http://localhost:5000")
      .then((res) => res.text())
      .then((data) => setMsg(data));
  }, []);

  return (
    <div>
      <h1>{msg}</h1>
    </div>
  );
}

export default App;

