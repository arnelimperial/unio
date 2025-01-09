import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
//import fs from "fs";
//import { fileURLToPath } from 'url';
//import path, { dirname } from 'path';

// Get the current directory name
//const __filename = fileURLToPath(import.meta.url);
//const __dirname = dirname(__filename);

// Load SSL certificate and key
// const sslKey = fs.readFileSync(path.resolve(__dirname, "../ssl/key.pem"));
// const sslCert = fs.readFileSync(path.resolve(__dirname, "../ssl/cert.pem"));

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0", // Allow access from the outside
    port: 5173,
  }, // needed for docker and running at https
  preview: {
    host: "0.0.0.0",
    port: 5173,
  }, // needed for docker and running at https
});
