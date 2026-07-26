/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        canvas: "#0A0F1C",
        panel: "#121A2B",
        "panel-raised": "#17213B",
        hairline: "#26314A",
        ink: "#E7ECF5",
        "ink-muted": "#8B96AE",
        "ink-dim": "#5B6784",
        signal: {
          teal: "#2FD3B0",
          amber: "#F5A93F",
          red: "#F2545B",
          indigo: "#7C93F7",
        },
      },
      fontFamily: {
        display: ["'Space Grotesk'", "sans-serif"],
        body: ["'Inter'", "sans-serif"],
        mono: ["'IBM Plex Mono'", "monospace"],
      },
      boxShadow: {
        panel: "0 1px 0 0 rgba(255,255,255,0.03) inset, 0 12px 24px -12px rgba(0,0,0,0.5)",
      },
    },
  },
  plugins: [],
};
