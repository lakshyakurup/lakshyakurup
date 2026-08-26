import os

svg_content = """<svg width="480" height="170" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" rx="12" fill="#1a1b26" stroke="#7aa2f7" stroke-width="1.5"/>
  <text x="25" y="35" font-family="Segoe UI, sans-serif" font-size="16" font-weight="bold" fill="#7aa2f7">⚡ Lakshya's System Status & Active Focus</text>
  <text x="25" y="65" font-family="Segoe UI, sans-serif" font-size="13" fill="#a9b1d6">• Core Stack: Full-Stack React / Next.js / Python</text>
  <text x="25" y="90" font-family="Segoe UI, sans-serif" font-size="13" fill="#a9b1d6">• Primary Domains: AI Web Apps & Cloud Infrastructure</text>
  <text x="25" y="115" font-family="Segoe UI, sans-serif" font-size="13" fill="#9ece6a">• Automation Pipeline: Active & Generating Local SVGs</text>
  <text x="25" y="140" font-family="Segoe UI, sans-serif" font-size="13" fill="#bb9af7">• Current Goal: Building Scalable Production-Ready Products</text>
</svg>"""

with open("profile-stats.svg", "w") as f:
    f.write(svg_content)
