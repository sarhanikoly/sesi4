def determine_winner(player1, player2):
    if player1 == player2:
        return "Seri"
    elif (player1 == "batu" and player2 == "gunting") or \
         (player1 == "gunting" and player2 == "kertas") or \
         (player1 == "kertas" and player2 == "batu"):
        return "Player 1"
    else:
        return "Player 2"

def main():
    print("Selamat datang di permainan Batu-Gunting-Kertas!")

    while True:
        player1 = input("Player 1, masukkan pilihan Anda (batu/gunting/kertas): ").lower()
        player2 = input("Player 2, masukkan pilihan Anda (batu/gunting/kertas): ").lower()

        if player1 not in ['batu', 'gunting', 'kertas'] or player2 not in ['batu', 'gunting', 'kertas']:
            print("Pilihan tidak valid. Harap masukkan 'batu', 'gunting', atau 'kertas'.")
            continue

        winner = determine_winner(player1, player2)
        print(f"Pemenangnya adalah: {winner}")

        play_again = input("Apakah Anda ingin bermain lagi? (ya/tidak): ").lower()
        if play_again != "ya":
            break

    print("Terima kasih telah bermain!")

if __name__ == "__main__":
    main()