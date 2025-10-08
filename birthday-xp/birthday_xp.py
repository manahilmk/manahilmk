from datetime import date

# --- CONFIG ---
dob = date(2000, 8, 12)
today = date.today()
total_bar_width = 260  # width of the XP bar in SVG

# --- AGE CALCULATION ---
current_age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    current_age -= 1

# --- NEXT BIRTHDAY ---
next_birthday_year = today.year
if (today.month, today.day) >= (dob.month, dob.day):
    next_birthday_year += 1
next_birthday = date(next_birthday_year, dob.month, dob.day)

last_birthday_year = next_birthday_year - 1
last_birthday = date(last_birthday_year, dob.month, dob.day)

# --- DAYS CALCULATION ---
days_since_birthday = (today - last_birthday).days
total_days_between_birthdays = (next_birthday - last_birthday).days
xp_percent = days_since_birthday / total_days_between_birthdays
fill_width = total_bar_width * xp_percent

# --- OUTPUT SVG ---
svg_template = f'''
<svg width="460" height="64" viewBox="0 0 460 64" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hex-fill" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#9be4ff"/>
      <stop offset="45%" stop-color="#6dd3ff"/>
      <stop offset="100%" stop-color="#8a6cff"/>
    </linearGradient>

    <linearGradient id="hex-frame" x1="0%" y1="0%" x2="1" y2="1">
      <stop offset="0%" stop-color="#fff6e6" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#ffd88a" stop-opacity="0.75"/>
    </linearGradient>

    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- outer frame -->
  <rect x="10" y="10" width="400" height="44" rx="18" ry="18" fill="#0f1012" stroke="url(#hex-frame)" stroke-width="2.2"/>

  <!-- left level -->
  <text x="50" y="36" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="#ffdca4" text-anchor="middle">Level {current_age}</text>

  <!-- centered bar background -->
  <rect x="80" y="16" width="260" height="32" rx="16" ry="16" fill="#17181a" stroke="#2a2a2a" stroke-width="1"/>

  <!-- progress fill -->
  <rect x="80" y="16" width="{fill_width}" height="32" rx="16" ry="16" fill="url(#hex-fill)" style="filter:url(#softGlow)"/>

  <!-- XP text inside bar -->
  <text x="210" y="36" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="#fff8e6" text-anchor="middle">{days_since_birthday} / {total_days_between_birthdays} XP</text>

  <!-- right level -->
  <text x="370" y="36" font-family="Georgia, 'Times New Roman', serif" font-size="13" fill="#ffdfa1" text-anchor="middle">Level {current_age + 1}</text>

  <!-- circle at far right outside main box -->
  <circle cx="430" cy="32" r="22" fill="#0b0c0d" stroke="url(#hex-frame)" stroke-width="2.2"/>

  <!-- compass-style pointer -->
  <polygon points="430,12 437,32 430,52 423,32" fill="#9be4ff" opacity="0.85">
    <animateTransform attributeName="transform" type="rotate" from="0 430 32" to="360 430 32" dur="9s" repeatCount="indefinite"/>
  </polygon>
</svg>
'''

with open("birthday-xp/birthday_xp.svg", "w") as f:
    f.write(svg_template)
