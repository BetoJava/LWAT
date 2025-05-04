import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import { Library } from 'lucide-react';
import { ThemeToggle } from '../common/ThemeToggle';

const navLinks = [
  { to: '/', label: 'Importer' },
  { to: '/explore', label: 'Explorer' }
];

const Header = () => (
  <header className="bg-white dark:bg-gray-800 shadow-sm">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <div className="flex justify-between items-center">
        <div className="flex items-center">
          <Link to="/" className="flex items-center group">
            <Library className="h-8 w-8 text-blue-600 dark:text-blue-500 mr-2 group-hover:scale-110 transition-transform" />
            <span className="text-xl font-bold">LWAT</span>
          </Link>
        </div>
        <nav className="flex gap-6 items-center">
          {navLinks.map(link => (
            <NavLink
              key={link.to}
              to={link.to}
              className={({ isActive }) =>
                `text-base font-medium transition-colors px-2 py-1 rounded hover:bg-blue-50 dark:hover:bg-gray-700 ${isActive ? 'text-blue-600 dark:text-blue-400 underline' : 'text-gray-700 dark:text-gray-200'}`
              }
              end={link.to === '/'}
            >
              {link.label}
            </NavLink>
          ))}
          <ThemeToggle />
        </nav>
      </div>
    </div>
  </header>
);

export default Header; 