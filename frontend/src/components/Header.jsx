import React from 'react';
import { Cpu } from 'lucide-react';

const Header = ({ status }) => {
    return (
        <header className="mb-12 flex items-center justify-between">
            <div className="flex items-center gap-3">
                <div className="p-2 bg-gradient-to-br from-indigo-500 to-cyan-500 rounded-lg">
                    <Cpu size={32} />
                </div>
                <div>
                    <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-500">
                        QuasiQ Optimizer
                    </h1>
                    <p className="text-gray-400 text-sm">Quantum-Inspired Distributed Annealing</p>
                </div>
            </div>
            <div className="glass-panel px-4 py-2 flex items-center gap-2">
                <div className={`w-3 h-3 rounded-full ${status === 'PROCESSING' ? 'bg-yellow-400 animate-pulse' : status === 'COMPLETED' ? 'bg-green-400' : 'bg-gray-400'}`}></div>
                <span className="text-sm font-mono uppercase">{status}</span>
            </div>
        </header>
    );
};

export default Header;
