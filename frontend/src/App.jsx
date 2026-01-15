import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import Controls from './components/Controls';
import TelemetryChart from './components/TelemetryChart';

// Configuration
const API_URL = 'http://localhost:8000/api';

function App() {
    const [config, setConfig] = useState({
        iterations: 1000,
        temperature: 100.0,
        cooling_rate: 0.95,
        function: 'rastrigin'
    });
    const [taskId, setTaskId] = useState(null);
    const [status, setStatus] = useState('IDLE'); // IDLE, PROCESSING, COMPLETED
    const [data, setData] = useState(null);
    const [polling, setPolling] = useState(false);

    const startOptimization = async () => {
        try {
            setStatus('PROCESSING');
            setData(null);
            const response = await axios.post(`${API_URL}/optimize`, config);
            setTaskId(response.data.task_id);
            setPolling(true);
        } catch (error) {
            console.error("Error starting optimization", error);
            setStatus('ERROR');
        }
    };

    useEffect(() => {
        if (!polling || !taskId) return;

        const interval = setInterval(async () => {
            try {
                const res = await axios.get(`${API_URL}/tasks/${taskId}`);
                if (res.data.status === 'SUCCESS') {
                    setData(res.data.result);
                    setStatus('COMPLETED');
                    setPolling(false);
                } else if (res.data.status === 'FAILURE') {
                    setStatus('ERROR');
                    setPolling(false);
                }
            } catch (e) {
                console.error("Polling error", e);
            }
        }, 1000);

        return () => clearInterval(interval);
    }, [polling, taskId]);

    return (
        <div className="min-h-screen p-8 text-white">
            <Header status={status} />
            <main className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <Controls
                    config={config}
                    setConfig={setConfig}
                    onStart={startOptimization}
                    status={status}
                />
                <TelemetryChart data={data} />
            </main>
        </div>
    )
}

export default App
