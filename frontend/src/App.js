import React, { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
    const [items, setItems] = useState([])

    useEffect(() => {
        axios.get('http://localhost:8000/items')
            .then(res => {
                setItems(res.data)
            })
            .catch(err => {
                console.error('Error fetching items:', err)
            })
    }, [])

    return (
        <div>
            <h1>Item List</h1>
            <ul>
                {items.map(item => (
                    <li key={item.id}>
                        {item.description} - ${item.price}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default App
