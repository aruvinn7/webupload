import pandas as pd
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

akun_file = os.path.join(settings.MEDIA_ROOT, "akun.xlsx")
vote_file = os.path.join(settings.MEDIA_ROOT, "vote.xlsx")

if os.path.exists(akun_file):
    df_akun = pd.read_excel(akun_file)
else:
    print("File akun.xlsx tidak ditemukan!")

akun = []

# LOGIN FUNCTION
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        nim = request.POST.get('username')
        password = request.POST.get('password')

        if not os.path.exists(akun_file):
            return HttpResponse("Database akun tidak ditemukan!")

        df = pd.read_excel(akun_file)
        dict_akun = dict(zip(df['nim'].astype(str), df['pass']))  

        if nim in dict_akun and dict_akun[nim] == password:
            request.session['nim'] = nim  
            messages.success(request, 'Login Berhasil!')

            # Reset akun setiap kali user login
            global akun
            akun = []  # Kosongkan dulu setiap login

            if nim == "112233":
                akun.append("delete")
                return redirect('read_vote') # Tambahkan "delete" hanya jika user 223344

            elif nim == 'panitiakmti2025' :
                return redirect('read_vote')
            
            return redirect('dashboard')

        else:
            messages.error(request, 'Login gagal, periksa kembali NIM dan Password!')
            return redirect('login')

def logout(request):
    request.session.flush()
    messages.success(request, 'Anda berhasil logout!')
    return redirect('login')
    

def dashboard(request):
    if request.method == 'GET':
        return render(request, 'vote/dashboard.html')
    else:
        if 'nim' not in request.session:
            messages.error(request, 'Anda belum login!')
            return redirect('login')

        nim = request.session['nim']  # Ambil NIM dari session
        vote_choice = request.POST.get('vote')
        print(vote_choice)


        if vote_choice == "True" :
            calon = "LANANG RIZQI BANTAR"
        else:
            calon = "DZIKRON FAUQO NIRWANA"

        if not os.path.exists(vote_file):
            df_vote = pd.DataFrame(columns=['nama', 'vote'])
        else:
            df_vote = pd.read_excel(vote_file)

        # Cek apakah user sudah melakukan vote sebelumnya
        if nim in df_vote['nama'].astype(str).values:
            messages.error(request, 'Anda sudah melakukan vote!')
            return redirect('dashboard')
        
        # Simpan vote dengan menambahkan data baru ke DataFrame
        new_vote = pd.DataFrame({'nama': [nim], 'vote': [calon]})
        df_vote = pd.concat([df_vote, new_vote], ignore_index=True)

        # Simpan kembali ke Excel
        df_vote.to_excel(vote_file, index=False)

        messages.success(request, 'Vote Berhasil!')
        return redirect('login')
    
def read_vote(request):
    if not os.path.exists(vote_file):
        votes = []
        total_lanang = 0
        total_dzikron = 0
    else:
        df_vote = pd.read_excel(vote_file)
        votes = df_vote.to_dict(orient='records')  

        # Hitung total suara untuk masing-masing kandidat
        total_lanang = (df_vote['vote'] == "LANANG RIZQI BANTAR").sum()
        total_dzikron = (df_vote['vote'] == "DZIKRON FAUQO NIRWANA").sum()

    return render(request, 'vote/read_vote.html', {
        'delete' : akun,
        'votes': votes,
        'total_lanang': total_lanang,
        'total_dzikron': total_dzikron
    })
    
def delete_vote(request):
    if 'nim' not in request.session:
        messages.error(request, 'Anda belum login!')
        return redirect('login')

    nim = request.session['nim']

    # Hanya NIM 223344 yang bisa menghapus vote
    if nim != "112233":
        messages.error(request, 'Anda tidak memiliki akses untuk menghapus vote!')
        return redirect('read_vote')

    if request.method == 'POST':
        selected_votes = request.POST.getlist('selected_votes')  # Ambil daftar vote yang dipilih
        
        if not selected_votes:
            messages.error(request, 'Tidak ada vote yang dipilih untuk dihapus!')
            return redirect('read_vote')

        if not os.path.exists(vote_file):
            messages.error(request, 'File vote.xlsx tidak ditemukan!')
            return redirect('read_vote')

        # Baca file vote.xlsx
        df_vote = pd.read_excel(vote_file)

        # Filter vote yang tidak terpilih agar tetap tersimpan
        df_vote = df_vote[~df_vote['nama'].astype(str).isin(selected_votes)]

        # Simpan perubahan ke file Excel
        df_vote.to_excel(vote_file, index=False)

        messages.success(request, 'Vote yang dipilih berhasil dihapus!')
        return redirect('read_vote')

    return redirect('read_vote')
