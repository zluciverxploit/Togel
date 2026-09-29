"""
==========================================================
   KALKULATOR MISTIK INDEX TOGEL - V5
   FITUR: 7 TAHAP RUMUS MISTIK + ANIMASI LOADING
   Developer : Ari Marshello
   Library   : Rich
==========================================================
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.align import Align
from rich.text import Text
from rich.rule import Rule
from rich.columns import Columns
from rich.tree import Tree
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.live import Live
from rich import box
import time
import os
import json
import random
from datetime import datetime

console = Console()

# ==========================================================
# KONFIGURASI
# ==========================================================
JUMLAH_TAHAP = 7

# Kecepatan animasi (detik)
DELAY_TAHAP    = 0.6   # jeda antar tahap
DELAY_TREE     = 0.3   # jeda tiap baris tree
DELAY_TABEL    = 0.4   # jeda tiap baris tabel
DELAY_LOADING  = 1.2   # jeda loading awal

# ==========================================================
# DATA MISTIK
# ==========================================================
MISTIK_LAMA  = {0: 8, 1: 7, 2: 6, 3: 9, 4: 5, 5: 4, 6: 2, 7: 1, 8: 0, 9: 3}
MISTIK_BARU  = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 0}
INDEX_NOGO   = {0: 5, 1: 6, 2: 7, 3: 8, 4: 9, 5: 0, 6: 1, 7: 2, 8: 3, 9: 4}
INDEX_KEPALA = {0: 5, 1: 6, 2: 7, 3: 8, 4: 9, 5: 0, 6: 1, 7: 2, 8: 3, 9: 4}
INDEX_EKOR   = {0: 9, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8}

SHIO = ["Tikus","Kerbau","Macan","Kelinci","Naga","Ular",
        "Kuda","Kambing","Monyet","Ayam","Anjing","Babi"]

WARNA_HOKI = {
    0:"Hitam", 1:"Putih", 2:"Merah", 3:"Kuning",
    4:"Hijau", 5:"Biru", 6:"Ungu", 7:"Emas",
    8:"Perak", 9:"Merah Muda"
}

ELEMEN = {
    0:"Air", 1:"Api", 2:"Tanah", 3:"Kayu", 4:"Logam",
    5:"Air", 6:"Api", 7:"Tanah", 8:"Kayu", 9:"Logam"
}

ARAH = {
    0:"Utara", 1:"Selatan", 2:"Barat Daya", 3:"Timur",
    4:"Barat", 5:"Timur Laut", 6:"Barat Laut", 7:"Tenggara",
    8:"Selatan", 9:"Barat"
}

RIWAYAT_FILE = "riwayat_togel_v5.json"

# ==========================================================
# FILE RIWAYAT
# ==========================================================
def load_riwayat():
    if os.path.exists(RIWAYAT_FILE):
        try:
            with open(RIWAYAT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def save_riwayat(data):
    with open(RIWAYAT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def tambah_riwayat(entry):
    data = load_riwayat()
    data.append(entry)
    save_riwayat(data)

# ==========================================================
# TAMPILAN & ANIMASI
# ==========================================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    title = Text()
    title.append("🎲  KALKULATOR MISTIK INDEX TOGEL  🎲\n", style="bold yellow")
    title.append("V5 - 7 TAHAP RUMUS MISTIK + LOADING DRAMATIS\n", style="bold bright_cyan")
    title.append("Developer : ", style="bold white")
    title.append("Ari Marshello", style="bold magenta")

    console.print(
        Panel(
            Align.center(title),
            border_style="bright_magenta",
            box=box.DOUBLE,
            padding=(1, 4),
        )
    )
    console.print()


def loading_awal(pesan="Membuka gerbang mistik..."):
    """Animasi loading awal dengan spinner & pesan berganti."""
    pesan_list = [
        "🔮 Membuka gerbang mistik...",
        "🕯️  Menyalakan lilin keberuntungan...",
        "📿 Membaca mantra angka...",
        "✨ Menghubungkan energi semesta...",
        "⚡ Menyiapkan rumus rahasia...",
    ]
    with console.status(f"[bold cyan]{pesan}[/bold cyan]", spinner="dots12") as status:
        for p in pesan_list:
            status.update(f"[bold cyan]{p}[/bold cyan]")
            time.sleep(0.35)


def progress_bar(label="Menghitung", durasi=1.2, warna="bright_green"):
    """Progress bar animasi dengan ETA."""
    with Progress(
        SpinnerColumn(style="bright_magenta", spinner_name="dots"),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(bar_width=40, style=warna, complete_style="bright_yellow"),
        TextColumn("[bold yellow]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(label, total=100)
        langkah = durasi / 100
        for _ in range(100):
            time.sleep(langkah)
            progress.update(task, advance=1)


def jeda_titik(pesan="Memproses", jumlah_titik=3, delay=0.35, warna="cyan"):
    """Animasi titik-titik bergerak."""
    for i in range(jumlah_titik):
        teks = f"[bold {warna}]⏳ {pesan}" + "." * (i + 1) + f"[/bold {warna}]"
        console.print(teks, end="\r")
        time.sleep(delay)
    console.print(" " * 60, end="\r")


def print_delay(renderable, delay=0.25):
    """Print dengan jeda biar muncul satu per satu."""
    console.print(renderable)
    time.sleep(delay)


# ==========================================================
# LOGIKA INTI - 7 TAHAP RUMUS MISTIK
# ==========================================================
def angka_ke_list(angka):
    return [int(d) for d in str(angka)]


def tujuh_tahap_mistik(angka, animasi=True):
    """
    7 tahap penjumlahan dengan RUMUS MISTIK BIASA.
    Kalau animasi=True, akan ada jeda di setiap tahap.
    """
    digit_awal = angka_ke_list(angka)
    jumlah_digit_awal = sum(digit_awal)
    tahap = []

    def tampil_tahap(t, delay=DELAY_TAHAP):
        if animasi:
            console.print(
                Panel(
                    Text.assemble(
                        (f"  ▶ TAHAP {t['tahap']}\n", "bold bright_cyan"),
                        (f"  📐 Rumus  : ", "bold white"), (t["rumus"], "bold green"),
                        ("\n  🧮 Detail : ", "bold white"), (t["detail"], "bold yellow"),
                        ("\n  🎯 Hasil  : ", "bold white"),
                        (f"{t['hasil']}", "bold white on bright_magenta"),
                    ),
                    border_style="bright_magenta",
                    box=box.ROUNDED,
                    padding=(0, 1),
                )
            )
            time.sleep(delay)

    # -------- TAHAP 1 --------
    h1 = jumlah_digit_awal
    t = {
        "tahap": 1,
        "rumus": "Jumlahkan semua digit awal",
        "detail": f"{' + '.join(map(str, digit_awal))}",
        "hasil": h1,
        "digit_hasil": angka_ke_list(h1),
    }
    tahap.append(t)
    tampil_tahap(t)

    # -------- TAHAP 2 --------
    d2 = angka_ke_list(h1)
    h2 = sum(d2)
    t = {
        "tahap": 2,
        "rumus": "Jumlahkan digit hasil Tahap 1",
        "detail": f"{' + '.join(map(str, d2))}",
        "hasil": h2,
        "digit_hasil": angka_ke_list(h2),
    }
    tahap.append(t)
    tampil_tahap(t)

    # -------- TAHAP 3 --------
    h3_raw = (h2 * 2) - jumlah_digit_awal
    h3 = abs(h3_raw)
    t = {
        "tahap": 3,
        "rumus": "(Hasil T2 × 2) − Jumlah Digit Awal",
        "detail": f"({h2} × 2) − {jumlah_digit_awal}",
        "hasil": h3,
        "digit_hasil": angka_ke_list(h3),
    }
    tahap.append(t)
    tampil_tahap(t)

    # -------- TAHAP 4 --------
    s3 = str(h3)
    if len(s3) >= 2:
        a4, b4 = int(s3[-2]), int(s3[-1])
        h4 = a4 + b4
        detail4 = f"{a4} + {b4}"
    else:
        h4 = h3
        detail4 = f"{h3}"
    t = {
        "tahap": 4,
        "rumus": "Jumlahkan 2 digit terakhir Tahap 3",
        "detail": detail4,
        "hasil": h4,
        "digit_hasil": angka_ke_list(h4),
    }
    tahap.append(t)
    tampil_tahap(t)

    # -------- TAHAP 5 --------
    d5 = angka_ke_list(h4)
    h5 = sum(d5)
    t = {
        "tahap": 5,
        "rumus": "Jumlahkan digit hasil Tahap 4",
        "detail": f"{' + '.join(map(str, d5))}",
        "hasil": h5,
        "digit_hasil": angka_ke_list(h5),
    }
    tahap.append(t)
    tampil_tahap(t)

    # -------- TAHAP 6 --------
    dgt_akhir = int(str(h5)[-1])
    mistik_akhir = MISTIK_LAMA[dgt_akhir]
    h6 = h5 + mistik_akhir
    t = {
        "tahap": 6,
        "rumus": "Hasil T5 + Mistik Lama(digit terakhir)",
        "detail": f"{h5} + Mistik Lama({dgt_akhir}={mistik_akhir})",
        "hasil": h6,
        "digit_hasil": angka_ke_list(h6),
    }
    tahap.append(t)
    tampil_tahap(t)

    # -------- TAHAP 7 --------
    d7 = angka_ke_list(h6)
    h7 = sum(d7)
    t = {
        "tahap": 7,
        "rumus": "Jumlahkan semua digit hasil Tahap 6",
        "detail": f"{' + '.join(map(str, d7))}",
        "hasil": h7,
        "digit_hasil": angka_ke_list(h7),
    }
    tahap.append(t)
    tampil_tahap(t)

    # -------- HASIL AKHIR --------
    final = h7
    if final > 9:
        final = sum(int(d) for d in str(final))

    return {
        "tahap": tahap,
        "deret": [t["hasil"] for t in tahap],
        "hasil_akhir": final,
        "digit_awal": digit_awal,
    }


def hitung_mistik_index(angka):
    digit = angka_ke_list(angka)
    hasil = {
        "Mistik Lama":   [MISTIK_LAMA[d] for d in digit],
        "Mistik Baru":   [MISTIK_BARU[d] for d in digit],
        "Index Nogo":    [INDEX_NOGO[d] for d in digit],
        "Index Kepala":  [INDEX_KEPALA[d] for d in digit],
        "Index Ekor":    [INDEX_EKOR[d] for d in digit],
    }
    if len(digit) >= 2:
        hasil["AS Mistik"]  = (digit[0] + digit[-1]) % 10
        hasil["KOP Mistik"] = (digit[0] + digit[1]) % 10
    else:
        hasil["AS Mistik"]  = digit[0]
        hasil["KOP Mistik"] = digit[0]
    hasil["Tesson"] = "".join(str((d + 1) % 10) for d in digit)
    hasil["Boom"]   = "".join(str((d - 1) % 10) for d in digit)
    return hasil


def generate_angka_jadi(angka, hasil_7x):
    digit = angka_ke_list(angka)
    a = digit[-1]
    b = MISTIK_LAMA[a]
    c = MISTIK_BARU[a]
    d = INDEX_NOGO[a]
    final = hasil_7x["hasil_akhir"]

    dasar = [b, c, d, final, a, (b + c) % 10, (c + d) % 10]

    return {
        "2D": "".join(map(str, dasar[2:4])),
        "3D": "".join(map(str, dasar[1:4])),
        "4D": "".join(map(str, dasar[:4])),
        "5D": "".join(map(str, dasar[:5])),
        "6D": "".join(map(str, dasar[:6])),
        "Colok Bebas": f"{b} / {final}",
        "Colok Naga": f"{b}{c}{final}",
        "Shio": SHIO[(final + a) % 12],
        "BBFS": "".join(map(str, dasar)),
        "Angka Utama (7x)": final,
    }


def info_keberuntungan(angka, final):
    digit = angka_ke_list(angka)
    return {
        "Elemen": ELEMEN[final],
        "Warna Hoki": WARNA_HOKI[final],
        "Arah Hoki": ARAH[final],
        "Shio": SHIO[(final + digit[-1]) % 12],
        "Angka Hoki Tambahan": (final * 7) % 100,
    }

# ==========================================================
# TAMPILAN HASIL
# ==========================================================
def tampilkan_tree_7tahap(angka, hasil, animasi=True):
    """Tree dengan animasi muncul baris per baris."""
    tree = Tree(f"[bold yellow]🌳 7 TAHAP RUMUS MISTIK — Angka [bold bright_cyan]{angka}[/bold bright_cyan][/bold yellow]")
    tree.add(f"[bold white]Digit Awal :[/bold white] [bold yellow]{' '.join(map(str, angka_ke_list(angka)))}[/bold yellow]")
    tree.add(f"[bold white]Total Awal :[/bold white] [bold green]{sum(angka_ke_list(angka))}[/bold green]")

    for t in hasil["tahap"]:
        node = tree.add(f"[bold cyan]TAHAP {t['tahap']}[/bold cyan] — [dim]{t['rumus']}[/dim]")
        node.add(f"[white]Detail  :[/white] [bold green]{t['detail']}[/bold green]")
        node.add(f"[white]Hasil   :[/white] [bold bright_yellow]{t['hasil']}[/bold bright_yellow]")
        if animasi:
            # re-render dengan jeda
            console.print(tree)
            time.sleep(DELAY_TREE)

    if not animasi:
        console.print(tree)
    console.print()


def tampilkan_ringkasan_7tahap(hasil, animasi=True):
    table = Table(
        title="📌 Ringkasan 7 Tahap Rumus Mistik",
        box=box.DOUBLE_EDGE, border_style="bright_magenta",
        header_style="bold cyan", title_style="bold yellow",
    )
    table.add_column("Tahap", justify="center", style="bold cyan")
    table.add_column("Rumus", justify="left", style="bold green")
    table.add_column("Detail", justify="center", style="bold white")
    table.add_column("Hasil", justify="center", style="bold bright_yellow")

    console.print(table)

    for t in hasil["tahap"]:
        table.add_row(f"T{t['tahap']}", t["rumus"], t["detail"], str(t["hasil"]))
        # Clear dan re-print untuk efek animasi
        if animasi:
            clear()
            banner()
            console.print(Rule("[bold bright_magenta]📌 Ringkasan 7 Tahap Rumus Mistik[/bold bright_magenta]"))
            console.print(table)
            time.sleep(DELAY_TABEL)

    console.print()

    deret = " → ".join(map(str, hasil["deret"]))

    # Animasi deret
    if animasi:
        console.print("[bold white]🔗 Membentuk deret...[/bold white]")
        time.sleep(0.4)

    console.print(Panel(
        Align.center(Text.assemble(
            ("🔗 Deret 7 Tahap:\n\n", "bold white"),
            (deret, "bold green"),
        )),
        border_style="bright_cyan", box=box.ROUNDED, padding=(1, 2),
    ))
    time.sleep(0.5)
    console.print()

    # Animasi hasil akhir
    if animasi:
        with console.status("[bold bright_magenta]🎯 Menghitung hasil akhir...[/bold bright_magenta]", spinner="bouncingBall"):
            time.sleep(DELAY_LOADING)

    panel = Panel(
        Align.center(
            Text.assemble(
                ("🎯 HASIL AKHIR (7 Tahap Rumus Mistik)\n\n", "bold white"),
                (f"   {hasil['hasil_akhir']}   ", "bold white on bright_magenta"),
            )
        ),
        border_style="bright_green",
        box=box.HEAVY,
        padding=(1, 4),
    )
    console.print(panel)
    time.sleep(0.6)
    console.print()


def tampilkan_hasil(angka, hasil_mistik, hasil_7x, prediksi, info, animasi=True):
    # Tabel mistik dengan animasi baris
    table = Table(
        title=f"📊 Hasil Mistik untuk Angka: [bold yellow]{angka}[/bold yellow]",
        box=box.ROUNDED, border_style="cyan",
        header_style="bold magenta", title_style="bold white",
    )
    table.add_column("Jenis Mistik", style="bold green", justify="left")
    table.add_column("Hasil", style="bold yellow", justify="left")

    console.print(table)
    for k, v in hasil_mistik.items():
        table.add_row(k, " - ".join(map(str, v)) if isinstance(v, list) else str(v))
        if animasi:
            clear()
            banner()
            console.print(Rule("[bold cyan]📊 Hasil Mistik[/bold cyan]"))
            console.print(table)
            time.sleep(0.15)

    console.print()
    if animasi:
        time.sleep(0.4)

    # Animasi masuk ke 7 tahap
    if animasi:
        jeda_titik("Masuk ke perhitungan 7 tahap", 3, 0.3, "bright_magenta")
        console.print()

    console.print(Rule(f"[bold bright_magenta]🔢 {JUMLAH_TAHAP} TAHAP RUMUS MISTIK BIASA[/bold bright_magenta]"))
    console.print()

    # Animasi 7 tahap satu per satu (sudah ada di dalam fungsi)
    hasil_7x_baru = tujuh_tahap_mistik(angka, animasi=animasi)

    time.sleep(0.5)
    tampilkan_ringkasan_7tahap(hasil_7x_baru, animasi=animasi)

    # Animasi loading sebelum prediksi
    if animasi:
        with console.status("[bold bright_green]🎯 Menyusun prediksi angka jadi...[/bold bright_green]", spinner="arrow3"):
            time.sleep(DELAY_LOADING)

    pred_table = Table(
        title=f"🎯 Prediksi Angka Jadi (dari hasil {JUMLAH_TAHAP} tahap)",
        box=box.HEAVY_EDGE, border_style="bright_green",
        header_style="bold cyan", title_style="bold yellow",
    )
    pred_table.add_column("Kategori", justify="center", style="bold white")
    pred_table.add_column("Angka", justify="center", style="bold bright_yellow")

    for k, v in prediksi.items():
        pred_table.add_row(k, str(v))
    console.print(pred_table)
    console.print()

    # Animasi ramalan
    if animasi:
        with console.status("[bold bright_magenta]🧧 Membaca ramalan keberuntungan...[/bold bright_magenta]", spinner="moon"):
            time.sleep(DELAY_LOADING)

    info_table = Table(
        title="🧧 Ramalan Keberuntungan",
        box=box.MINIMAL_DOUBLE_HEAD, border_style="bright_magenta",
        header_style="bold yellow", title_style="bold bright_cyan",
    )
    info_table.add_column("Aspek", style="bold green")
    info_table.add_column("Nilai", style="bold bright_white")
    for k, v in info.items():
        info_table.add_row(k, str(v))
    console.print(info_table)
    console.print()


# ==========================================================
# MENU
# ==========================================================
def menu_utama():
    menu = Table(
        title=f"🏠 MENU UTAMA - V5 (7 Tahap + Loading)",
        box=box.HEAVY_EDGE, border_style="bright_cyan",
        title_style="bold yellow", header_style="bold magenta",
    )
    menu.add_column("No", justify="center", style="bold yellow")
    menu.add_column("Fitur", style="bold white")
    menu.add_column("Keterangan", style="dim")

    fitur = [
        ("1", "🔮 Hitung Mistik + 7 Tahap",  "Hitung mistik + 7 tahap rumus mistik + loading"),
        ("2", "🎯 Multi-Angka + 7 Tahap",    "Banyak angka sekaligus (2D-6D)"),
        ("3", "📅 Prediksi dari Tanggal",     "Konversi tanggal + 7 tahap"),
        ("4", "🔢 Analisa 4D Lengkap",        "AS/KOP/KEPALA/EKOR + 7 tahap per posisi"),
        ("5", "📜 Riwayat Perhitungan",        "Lihat & kelola riwayat"),
        ("6", "🎰 Generator Angka Hoki",       "Random + 7 tahap"),
        ("7", "🧧 Ramalan Keberuntungan",      "Elemen, warna, arah hoki"),
        ("8", "📊 Statistik Digit",            "Analisa frekuensi digit"),
        ("9", "🔍 Cek Angka vs Riwayat",       "Cocokkan histori"),
        ("0", "🚪 Keluar",                      "Keluar dari program"),
    ]

    for no, nama, ket in fitur:
        menu.add_row(no, nama, ket)

    console.print(menu)
    console.print()


# ==========================================================
# FITUR 1 : HITUNG MISTIK + 7 TAHAP
# ==========================================================
def fitur_hitung():
    banner()
    console.print(Rule("[bold cyan]🔮 HITUNG MISTIK + 7 TAHAP RUMUS MISTIK[/bold cyan]"))
    console.print("[dim]Support 2D sampai 6D (contoh: 12, 123, 1234, 12345, 123456)[/dim]")
    angka = Prompt.ask("[bold cyan]Masukkan angka (2-6 digit)[/bold cyan]")
    if not angka.isdigit() or not (2 <= len(angka) <= 6):
        console.print("[bold red]✖ Input tidak valid! Harus 2-6 digit angka.[/bold red]\n")
        Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")
        return

    # Animasi loading awal
    loading_awal("🔮 Membuka gerbang mistik untuk angka " + angka)
    progress_bar(f"Menghitung 7 tahap untuk {angka}", durasi=1.5)

    hasil_mistik = hitung_mistik_index(angka)
    hasil_7x = tujuh_tahap_mistik(angka, animasi=False)
    prediksi = generate_angka_jadi(angka, hasil_7x)
    info = info_keberuntungan(angka, hasil_7x["hasil_akhir"])

    time.sleep(0.4)
    tampilkan_hasil(angka, hasil_mistik, hasil_7x, prediksi, info, animasi=True)

    # Animasi simpan
    with console.status("[bold green]💾 Menyimpan ke riwayat...[/bold green]", spinner="simpleDotsScrolling"):
        time.sleep(0.8)
        tambah_riwayat({
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "angka": angka,
            "deret_7x": hasil_7x["deret"],
            "hasil_akhir": hasil_7x["hasil_akhir"],
            "prediksi": prediksi,
        })

    console.print("[green]✔ Hasil disimpan ke riwayat.[/green]\n")
    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# FITUR 2 : MULTI ANGKA
# ==========================================================
def fitur_multi():
    banner()
    console.print(Rule("[bold cyan]🎯 MULTI-ANGKA + 7 TAHAP[/bold cyan]"))
    inp = Prompt.ask("[bold cyan]Masukkan angka dipisah koma (contoh: 1234,56789,12)[/bold cyan]")
    daftar = [x.strip() for x in inp.split(",") if x.strip().isdigit() and 2 <= len(x.strip()) <= 6]

    if not daftar:
        console.print("[bold red]✖ Tidak ada angka valid (2-6 digit)![/bold red]\n")
        Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")
        return

    loading_awal(f"🔮 Menyiapkan {len(daftar)} angka untuk dihitung")

    table = Table(
        title="📋 Hasil Multi-Angka + 7 Tahap Rumus Mistik",
        box=box.DOUBLE_EDGE, border_style="bright_magenta",
        header_style="bold cyan", title_style="bold yellow",
    )
    table.add_column("Angka", style="bold yellow", justify="center")
    table.add_column("Digit", style="dim", justify="center")
    for i in range(1, JUMLAH_TAHAP + 1):
        table.add_column(f"T{i}", style="bold green", justify="center")
    table.add_column("Final", style="bold bright_magenta", justify="center")
    table.add_column("2D", style="bold cyan", justify="center")
    table.add_column("4D", style="bold cyan", justify="center")

    console.print(table)
    console.print()

    for a in daftar:
        with console.status(f"[bold cyan]🔄 Memproses angka {a}...[/bold cyan]", spinner="dots"):
            time.sleep(0.6)
            h7 = tujuh_tahap_mistik(a, animasi=False)
            p = generate_angka_jadi(a, h7)
            row = [a, f"{len(a)}D"] + [str(x) for x in h7["deret"]] + [str(h7["hasil_akhir"]), p["2D"], p["4D"]]
            table.add_row(*row)

        # Re-render table setiap baris
        clear()
        banner()
        console.print(Rule("[bold bright_magenta]📋 Hasil Multi-Angka[/bold bright_magenta]"))
        console.print(table)
        console.print()
        time.sleep(0.3)

    console.print("[green]✔ Selesai memproses semua angka![/green]\n")
    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# FITUR 3 : PREDIKSI DARI TANGGAL
# ==========================================================
def fitur_tanggal():
    banner()
    console.print(Rule("[bold cyan]📅 PREDIKSI DARI TANGGAL LAHIR + 7 TAHAP[/bold cyan]"))
    tgl = Prompt.ask("[bold cyan]Masukkan tanggal (DD-MM-YYYY)[/bold cyan]")
    try:
        d, m, y = map(int, tgl.replace("/", "-").split("-"))
        angka = f"{d:02d}{m:02d}{str(y)[-2:]}"
        if len(angka) > 4:
            angka = angka[-4:]
    except:
        console.print("[bold red]✖ Format tanggal salah![/bold red]\n")
        Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")
        return

    loading_awal(f"📅 Mengkonversi tanggal {tgl}")
    progress_bar("Mengubah tanggal ke angka mistik", durasi=1.0)

    hasil_mistik = hitung_mistik_index(angka)
    hasil_7x = tujuh_tahap_mistik(angka, animasi=False)
    prediksi = generate_angka_jadi(angka, hasil_7x)
    info = info_keberuntungan(angka, hasil_7x["hasil_akhir"])

    console.print(f"\n[bold yellow]Angka konversi:[/bold yellow] [bold bright_green]{angka}[/bold bright_green]\n")
    time.sleep(0.5)
    tampilkan_hasil(angka, hasil_mistik, hasil_7x, prediksi, info, animasi=True)
    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# FITUR 4 : ANALISA 4D
# ==========================================================
def fitur_analisa_4d():
    banner()
    console.print(Rule("[bold cyan]🔢 ANALISA 4D + 7 TAHAP RUMUS MISTIK[/bold cyan]"))
    angka = Prompt.ask("[bold cyan]Masukkan 4 digit angka[/bold cyan]")
    if not angka.isdigit() or len(angka) != 4:
        console.print("[bold red]✖ Harus 4 digit angka![/bold red]\n")
        Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")
        return

    loading_awal("🔢 Menganalisa struktur 4D")
    progress_bar("Membaca AS/KOP/KEPALA/EKOR", durasi=1.0)

    as_, kop, kepala, ekor = [int(d) for d in angka]

    tree = Tree("[bold yellow]🎯 Struktur Angka[/bold yellow]")
    tree.add(f"[bold cyan]AS[/bold cyan]     : [bold bright_white]{as_}[/bold bright_white] (Mistik: {MISTIK_LAMA[as_]})")
    time.sleep(0.2); console.print(tree)
    tree.add(f"[bold cyan]KOP[/bold cyan]    : [bold bright_white]{kop}[/bold bright_white] (Mistik: {MISTIK_LAMA[kop]})")
    time.sleep(0.2); console.print(tree)
    tree.add(f"[bold cyan]KEPALA[/bold cyan] : [bold bright_white]{kepala}[/bold bright_white] (Mistik: {MISTIK_LAMA[kepala]})")
    time.sleep(0.2); console.print(tree)
    tree.add(f"[bold cyan]EKOR[/bold cyan]   : [bold bright_white]{ekor}[/bold bright_white] (Mistik: {MISTIK_LAMA[ekor]})")
    time.sleep(0.2); console.print(tree)
    console.print()

    time.sleep(0.4)
    console.print(Rule("[bold bright_magenta]🔢 7 TAHAP PENJUMLAHAN[/bold bright_magenta]"))
    console.print()

    h7 = tujuh_tahap_mistik(angka, animasi=True)
    time.sleep(0.4)
    tampilkan_ringkasan_7tahap(h7, animasi=True)

    # Animasi per posisi
    with console.status("[bold bright_magenta]🧮 Menghitung 7 tahap per posisi...[/bold bright_magenta]", spinner="dots12"):
        time.sleep(DELAY_LOADING)

    posisi_table = Table(
        title="🧮 7 Tahap per Posisi (AS/KOP/KEPALA/EKOR)",
        box=box.HEAVY_HEAD, border_style="bright_magenta",
        header_style="bold cyan", title_style="bold yellow",
    )
    posisi_table.add_column("Posisi", style="bold green", justify="center")
    posisi_table.add_column("Nilai", style="bold bright_white", justify="center")
    posisi_table.add_column("Mistik", style="bold yellow", justify="center")
    posisi_table.add_column("Deret 7 Tahap", style="bold bright_magenta", justify="center")
    posisi_table.add_column("Final", style="bold bright_cyan", justify="center")

    console.print(posisi_table)

    for nama, val in [("AS", as_), ("KOP", kop), ("KEPALA", kepala), ("EKOR", ekor)]:
        mistik = MISTIK_LAMA[val]
        h = tujuh_tahap_mistik(str(mistik), animasi=False)
        deret = " → ".join(map(str, h["deret"]))
        posisi_table.add_row(nama, str(val), str(mistik), deret, str(h["hasil_akhir"]))

        clear()
        banner()
        console.print(Rule("[bold bright_magenta]🧮 7 Tahap per Posisi[/bold bright_magenta]"))
        console.print(posisi_table)
        time.sleep(0.5)

    console.print()
    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# FITUR 5 : RIWAYAT
# ==========================================================
def fitur_riwayat():
    banner()
    console.print(Rule("[bold cyan]📜 RIWAYAT PERHITUNGAN[/bold cyan]"))

    with console.status("[bold cyan]📂 Membaca riwayat...[/bold cyan]", spinner="dots"):
        time.sleep(0.7)
        data = load_riwayat()

    if not data:
        console.print("[yellow]Belum ada riwayat.[/yellow]\n")
    else:
        table = Table(
            title=f"Total: {len(data)} riwayat",
            box=box.MINIMAL_DOUBLE_HEAD, border_style="bright_cyan",
            header_style="bold magenta", title_style="bold yellow",
        )
        table.add_column("No", style="bold yellow", justify="center")
        table.add_column("Tanggal", style="dim")
        table.add_column("Angka", style="bold cyan", justify="center")
        table.add_column("Deret 7x", style="bold green")
        table.add_column("Final", style="bold bright_magenta", justify="center")
        table.add_column("2D", style="bold yellow", justify="center")
        table.add_column("4D", style="bold yellow", justify="center")

        console.print(table)

        for i, item in enumerate(data, 1):
            deret = " → ".join(map(str, item.get("deret_7x", [])))
            table.add_row(
                str(i), item.get("tanggal", "-"),
                item.get("angka", "-"),
                deret or "-",
                str(item.get("hasil_akhir", "-")),
                item.get("prediksi", {}).get("2D", "-"),
                item.get("prediksi", {}).get("4D", "-"),
            )
            clear()
            banner()
            console.print(Rule("[bold cyan]📜 Riwayat Perhitungan[/bold cyan]"))
            console.print(table)
            time.sleep(0.08)

        console.print()

        if Confirm.ask("[bold red]Hapus semua riwayat?[/bold red]", default=False):
            with console.status("[bold red]🗑️  Menghapus riwayat...[/bold red]", spinner="dots"):
                time.sleep(0.8)
                save_riwayat([])
            console.print("[green]✔ Riwayat dihapus.[/green]\n")

    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# FITUR 6 : GENERATOR
# ==========================================================
def fitur_generator():
    banner()
    console.print(Rule("[bold cyan]🎰 GENERATOR ANGKA HOKI + 7 TAHAP[/bold cyan]"))
    jumlah = IntPrompt.ask("[bold cyan]Berapa angka yang mau di-generate?[/bold cyan]", default=5)

    loading_awal("🎰 Mengocok angka keberuntungan")
    progress_bar("Mengacak & menghitung", durasi=1.5)

    table = Table(
        title="🍀 Angka Hoki Random + 7 Tahap Rumus Mistik",
        box=box.DOUBLE, border_style="bright_green",
        header_style="bold cyan", title_style="bold yellow",
    )
    table.add_column("No", justify="center", style="bold yellow")
    table.add_column("Angka", style="bold cyan", justify="center")
    table.add_column("Deret 7x", style="bold green")
    table.add_column("Final", style="bold bright_magenta", justify="center")
    table.add_column("2D", style="bold bright_yellow", justify="center")
    table.add_column("Shio", style="bold magenta", justify="center")

    console.print(table)

    for i in range(1, jumlah + 1):
        with console.status(f"[bold cyan]🎲 Mengacak angka ke-{i}...[/bold cyan]", spinner="dots"):
            time.sleep(0.5)
            angka = f"{random.randint(0,999999):06d}"
            h7 = tujuh_tahap_mistik(angka, animasi=False)
            p = generate_angka_jadi(angka, h7)
            deret = " → ".join(map(str, h7["deret"]))
            table.add_row(str(i), angka, deret, str(h7["hasil_akhir"]), p["2D"], p["Shio"])

        clear()
        banner()
        console.print(Rule("[bold bright_green]🎰 Generator Angka Hoki[/bold bright_green]"))
        console.print(table)
        time.sleep(0.2)

    console.print()
    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# FITUR 7 : RAMALAN
# ==========================================================
def fitur_ramalan():
    banner()
    console.print(Rule("[bold cyan]🧧 RAMALAN KEBERUNTUNGAN[/bold cyan]"))
    angka = Prompt.ask("[bold cyan]Masukkan angka kesukaanmu (2-6 digit)[/bold cyan]")
    if not angka.isdigit() or not (2 <= len(angka) <= 6):
        console.print("[bold red]✖ Input tidak valid![/bold red]\n")
        Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")
        return

    loading_awal("🧧 Memanggil dewi keberuntungan")
    progress_bar("Menghitung ramalan", durasi=1.2)

    h7 = tujuh_tahap_mistik(angka, animasi=False)
    final = h7["hasil_akhir"]
    info = info_keberuntungan(angka, final)

    deret = " → ".join(map(str, h7["deret"]))

    # Animasi deret
    console.print("[bold white]🔗 Deret 7 Tahap:[/bold white]")
    console.print(f"   [bold green]{deret}[/bold green]")
    time.sleep(0.4)
    console.print(f"[bold yellow]Hasil Akhir:[/bold yellow] [bold bright_magenta]{final}[/bold bright_magenta]\n")
    time.sleep(0.4)

    with console.status("[bold bright_magenta]✨ Membaca energi angka...[/bold bright_magenta]", spinner="moon"):
        time.sleep(1.0)

    panels = []
    for k, v in info.items():
        text = Text()
        text.append(f"{k}\n", style="bold white")
        text.append(str(v), style="bold yellow")
        panels.append(Panel(Align.center(text), border_style="bright_magenta",
                            box=box.ROUNDED, padding=(1, 2)))

    # Animasi panel muncul satu-satu
    for p in panels:
        console.print(p)
        time.sleep(0.25)

    console.print()
    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# FITUR 8 : STATISTIK
# ==========================================================
def fitur_statistik():
    banner()
    console.print(Rule("[bold cyan]📊 STATISTIK DIGIT[/bold cyan]"))
    angka = Prompt.ask("[bold cyan]Masukkan deret angka[/bold cyan]")
    if not angka.isdigit():
        console.print("[bold red]✖ Harus angka![/bold red]\n")
        Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")
        return

    loading_awal("📊 Menganalisa frekuensi digit")
    progress_bar("Membaca statistik", durasi=1.0)

    counter = {i: 0 for i in range(10)}
    for d in angka:
        counter[int(d)] += 1

    table = Table(
        title="📈 Frekuensi Digit",
        box=box.HEAVY_HEAD, border_style="bright_cyan",
        header_style="bold magenta", title_style="bold yellow",
    )
    table.add_column("Digit", justify="center", style="bold cyan")
    table.add_column("Frekuensi", justify="center", style="bold yellow")
    table.add_column("Bar", style="bold green")

    maks = max(counter.values()) if counter.values() else 1

    console.print(table)

    for d, c in counter.items():
        bar = "█" * int((c / maks) * 30) if maks else ""
        table.add_row(str(d), str(c), bar)
        clear()
        banner()
        console.print(Rule("[bold cyan]📊 Statistik Digit[/bold cyan]"))
        console.print(table)
        time.sleep(0.15)

    console.print()

    total = sum(int(d) for d in angka)
    with console.status("[bold cyan]🔮 Menghitung 7 tahap dari total...[/bold cyan]", spinner="dots"):
        time.sleep(0.8)
        h7_total = tujuh_tahap_mistik(str(total), animasi=False)

    deret = " → ".join(map(str, h7_total["deret"]))

    console.print(Panel(
        Align.center(Text.assemble(
            ("📌 Total Digit: ", "bold white"),
            (f"{total}\n", "bold yellow"),
            ("7 Tahap: ", "bold white"),
            (f"{deret}\n", "bold green"),
            ("Hasil Akhir: ", "bold white"),
            (f"{h7_total['hasil_akhir']}", "bold bright_magenta"),
        )),
        border_style="bright_magenta", box=box.ROUNDED, padding=(1, 2),
    ))
    console.print()
    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# FITUR 9 : CEK RIWAYAT
# ==========================================================
def fitur_cek_riwayat():
    banner()
    console.print(Rule("[bold cyan]🔍 CEK ANGKA VS RIWAYAT[/bold cyan]"))
    angka = Prompt.ask("[bold cyan]Masukkan angka untuk dicek[/bold cyan]")

    with console.status("[bold cyan]🔍 Mencari di riwayat...[/bold cyan]", spinner="dots"):
        time.sleep(0.8)
        data = load_riwayat()

    cocok = [x for x in data if x.get("angka") == angka]

    if cocok:
        console.print(f"[bold green]✔ Ditemukan {len(cocok)} kecocokan![/bold green]\n")
        for item in cocok:
            deret = " → ".join(map(str, item.get("deret_7x", [])))
            console.print(
                f"  • {item['tanggal']} → Angka: [bold yellow]{item['angka']}[/bold yellow] "
                f"| Deret: [bold green]{deret}[/bold green] "
                f"| Final: [bold bright_magenta]{item.get('hasil_akhir','-')}[/bold bright_magenta]"
            )
            time.sleep(0.15)
    else:
        console.print("[bold red]✖ Tidak ditemukan di riwayat.[/bold red]")

    console.print()
    Prompt.ask("[dim]Tekan Enter untuk kembali[/dim]", default="")


# ==========================================================
# MAIN
# ==========================================================
def main():
    loading_awal("🚀 Memulai program mistik...")

    while True:
        banner()
        menu_utama()
        pilihan = Prompt.ask("[bold cyan]Pilih menu[/bold cyan]", default="1")

        if pilihan == "1":
            fitur_hitung()
        elif pilihan == "2":
            fitur_multi()
        elif pilihan == "3":
            fitur_tanggal()
        elif pilihan == "4":
            fitur_analisa_4d()
        elif pilihan == "5":
            fitur_riwayat()
        elif pilihan == "6":
            fitur_generator()
        elif pilihan == "7":
            fitur_ramalan()
        elif pilihan == "8":
            fitur_statistik()
        elif pilihan == "9":
            fitur_cek_riwayat()
        elif pilihan == "0":
            with console.status("[bold bright_magenta]👋 Menutup program...[/bold bright_magenta]", spinner="dots"):
                time.sleep(1.0)
            console.print(
                Panel(
                    Align.center(Text(
                        "Terima kasih sudah memakai script ini!\n~ Ari Marshello ~",
                        style="bold cyan",
                    )),
                    border_style="bright_magenta",
                    box=box.DOUBLE,
                )
            )
            break
        else:
            console.print("[bold red]✖ Pilihan tidak valid![/bold red]\n")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Program dihentikan oleh user.[/bold red]")