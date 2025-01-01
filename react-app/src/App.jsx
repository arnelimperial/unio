import { lazy } from "react";
import { Toaster } from "react-hot-toast";
import "./styles.css";

const RouterList = lazy(() => import("./components/RouterList.tsx"));
const HeaderNav = lazy(() => import("./components/HeaderNav.jsx"));

function App() {
  return (
    <>
      <HeaderNav />
      <main className="container">
        <Toaster
          toastOptions={{
            duration: 5000,
          }}
        />
        <RouterList />
      </main>
    </>
  );
}

export default App;
