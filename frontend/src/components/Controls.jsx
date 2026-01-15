import React from 'react';
import { Zap, Play } from 'lucide-react';

const Controls = ({ config, setConfig, onStart, status }) => {
    return (
        <div className="glass-panel p-6 h-fit">
            <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
                <Zap className="text-yellow-400" /> Configuration
            </h2>

            <div className="space-y-4">
                <div>
                    <label className="block text-sm text-gray-400 mb-1">Objective Function</label>
                    <select
                        className="input-field bg-[#0c0c1d] cursor-pointer"
                        value={config.function}
                        onChange={(e) => setConfig({ ...config, function: e.target.value })}
                    >
                        <option value="rastrigin">Rastrigin (Multi-modal)</option>
                        <option value="rosenbrock">Rosenbrock (Valley)</option>
                        <option value="sphere">Sphere (Convex)</option>
                    </select>
                </div>

                <div>
                    <label className="block text-sm text-gray-400 mb-1">Iterations</label>
                    <input
                        type="number"
                        className="input-field"
                        value={config.iterations}
                        onChange={(e) => setConfig({ ...config, iterations: parseInt(e.target.value) })}
                    />
                </div>
                <div>
                    <label className="block text-sm text-gray-400 mb-1">Initial Temperature</label>
                    <input
                        type="number"
                        className="input-field"
                        value={config.temperature}
                        onChange={(e) => setConfig({ ...config, temperature: parseFloat(e.target.value) })}
                    />
                </div>
                <div>
                    <label className="block text-sm text-gray-400 mb-1">Cooling Rate (0-1)</label>
                    <input
                        type="number"
                        step="0.01"
                        className="input-field"
                        value={config.cooling_rate}
                        onChange={(e) => setConfig({ ...config, cooling_rate: parseFloat(e.target.value) })}
                    />
                </div>

                <button
                    onClick={onStart}
                    disabled={status === 'PROCESSING'}
                    className="btn-primary w-full flex items-center justify-center gap-2 mt-4"
                >
                    {status === 'PROCESSING' ? 'Optimizing...' : <><Play size={18} /> Initialize System</>}
                </button>
            </div>
        </div>
    );
};

export default Controls;
