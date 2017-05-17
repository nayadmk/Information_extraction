# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:57:06 2017

@author: Nayadmk
"""

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, label):
    # create directed networkx graph
    G = nx.Graph()

    # add edges
    G.add_edges_from(graph)
    graph_pos = nx.shell_layout(G)
    #graph_pos = nx.spectral_layout(G)
    #graph_pos = nx.spring_layout(G)
    #graph_pos = nx.random_layout(G)

    # draw nodes, edges and labels
    nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)

    # we can now added edge thickness and edge color
    nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='green')
    nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=label)

    plt.show()
#['Congressional Research', 'Institute', 'Science', 'International', 'North Korea', 'ICBM', 'ICBM']
    
    
entity = [['Adik', 'Presiden', 'Susilo Bambang Yudhoyono', 'Antasari', 'Bareskim', 'Sulawesi Selatan', 'Nasrudin', 'Makasar', 'Direktur PT Putra Rajawali Banjaran', 'Antasari Azhar Akhirnya Tepati Janji', 'Bareskrim Polri', 'Pihak', 'Andi Syamsuddin', 'Antasari Azhar', 'Nasrudin Zulkarnaen', 'Hary Tanoesodibjo', 'Pak Antasari'], ['Chanda M. Hamzah', 'Kasus Ruilslag Badan Urusan Logistik', 'Antasari', 'Al', 'Jaksa Urip Tri Gunawan', 'Polri', 'Pengadilan Tindak Pidana Korupsi Jakarta', 'Nasrudin Zulkarnaen Antasari Azhar', 'Gub Jakarta', 'Kejaksaan Jakarta Selatan', 'Selasa', 'Pak Beye', 'Kabupaten Bintan', 'Nasrudin Zulkarnaen', 'Ketua Komisi Pemberantasan Korupsi', 'Kejaksaan Negeri Jakarta Selatan', 'Untuk', 'Artalyta Suryani', 'Hutomo Mandala Putra', 'Ketua KPK Antasari Azhar', 'Agus', 'Bantuan Likuiditas Bank', 'Tommy Soeharto', 'Kepala Kejaksaan Negeri Jakarta Selatan Nama Antasari Azhar', 'Nama', 'Aulia Pohan', 'Sjamsul Nursalim', 'Hakim Agung Syafiuddin Kartasasmita', 'Komisi Pemberantasan Korupsi', 'Inilah', 'Presiden Joko Widodo', 'Komisi III DPR', 'Ayin', 'Al Amin Nur Nasution', 'Kota Tangerang', 'Jakarta Selasa', 'Pada', 'Mahkamah Agung', 'Putra Rajawali Banjaran', 'Susilo Bambang Yudhoyono', 'Agus Yudhoyono', 'Padang Golf Modernland', 'Pengadilan Tinggi', 'Aulia', 'Antasari Azhar', 'Penahanan', 'Sedangkan', 'Bareskrim', 'Jaksa Urip', 'Yayasan Pengembangan Perbankan'], ['Siapa', 'Antasari', 'Tuduhan Antasari', 'Edhie Baskoro', 'Direktur Putra Rajawali Banjaran', 'Aulia', 'Tujuan', 'Bareskrim Polri', 'Aulia Tantowi Pohan', 'Fitnah Keji Antasari', 'Deputi Gubernur Bank Indonesia', 'Ketua KPK Antasari Azhar', 'Ansari', 'Mantan Presiden Susilo Bambang Yudhoyono', 'Bilang2', 'Ibas', 'Sarah Sechan', 'Allah Swt', 'Dalam', 'Cikeas', 'Janganlah', 'Wahai Rakyatku', 'Agus', 'Habibie', 'Yudhoyono Selain SBY', 'Aulia Pohan', 'Nasrudin Zulkarnaen', 'Arie Keriting', 'Pelawak', 'Edhie', 'Marilah', 'Susilo Bambang Yudhoyono', 'Pilkada Jakarta', 'Sangat', 'Twitter', 'Tujuan Antasari', 'Pilgub Jakarta Antasari Azhar'], ['Kepala Lapas Tangerang', 'Tangerang', 'Antasari', 'Hotel Grand Mahakam', 'Kapolda', 'Metro Jaya', 'Hari Pahlawan', 'Aulia Pohan', 'Nasrudin Zulkarnaen', 'Kasubtit Pidana Khusus', 'Irjen Pol Wahyono', 'Rani Juliani', 'Kejaksaan Agung', 'Kepala Lembaga Pemasyarakatan Tangerang', 'Susilo Bambang Yudhoyono', 'Banyak', 'Ketua KPK', 'Padang Golf Modernland', 'Nasrudin', 'Allah', 'Nasrudin Zulkarnain', 'Antasari Azhar', 'Mendapat', 'Hukum'], ['Antasari', 'Badan Reserse Kriminal Polri', 'Bareskrim Polri', 'Kementerian Kelautan', 'Adalah', 'Ketua KPK Antasari Azhar', 'Anda', 'Jl Medan Merdeka Timur', 'Martinus', 'Gedung Divisi Humas', 'Kabag', 'Maaf', 'Kabid Humas Polda Metro Jaya', 'Perikanan', 'Nasrudin Zulkarnaen', 'Nasruddin Zulkarnaen', 'Rajawali Putra Banjaran', 'Jalan Trunojoyo', 'Bareskrim', 'Kasus Antasari Azhar Jakarta', 'Nasrudin', 'Mabes Polri', 'Jakarta Selatan', 'Jakarta Pusat', 'Masih Selidiki Unsur Sangkaan Palsu', 'Pak Antasari'], ['Agus Harimurti', 'Antasari', 'Kejaksaan Bulgaria', 'Hotel Grand Mahakam', 'Anatasari', 'Tim', 'Yayasan Pengembangan Bank Indonesia', 'Kepolisian Inggris', 'Kalau', 'Ahok', 'Inggris', 'Paslon', 'Dan', 'Nasaruddin', 'Ketua KPK Jilid II', 'Dari', 'Alexander Litvinenko', 'Cikeas', 'Munim Idris', 'Menurut Antasari', 'Andrei Luginov', 'Pengadilan Tipikor', 'Litvinenko', 'Pencari Fakta', 'Waterloo', 'Aulia Pohan', 'Jokowi', 'Hasil', 'Badan Intelijen Nasional', 'Pembunuhan', 'Harytanoe', 'Rani Juliani', 'Nasruddin Zulkarnaen', 'Munir', 'Tanggerang', 'Tim Pencari Fakta Pembunuhan Munir', 'Tipikor', 'Anazari', 'Hari', 'Dirut Putra Rajawali Banjaran', 'Nasrudin', 'Ketua KPK', 'Rani', 'Pilgub', 'Tim Pencari Fakta', 'Antasari Azhar', 'Nasruddin', 'London', 'Hary', 'Dmitry Kovtum', 'Georgy Markov', 'Kalau SBY Bukan Dalang Kasus Antasari Azhar Kata Antasari Azhar', 'Modern Land'], ['Pemilu Legislatif', 'Andi', 'Tangerang', 'Antasari', 'Mencari', 'Edhie Baskoro Yudhoyono', 'Hotel Grand Mahakam', 'Anda', 'Nyanyian Antasari Azhar', 'Jadi', 'Bareskrim Polri', 'Bapak Susilo Bambang Yudhoyono', 'Apakah', 'Pilkada', 'Andi Syamsudin', 'Pak', 'Pilkada DKI', 'Pengadilan Tipikor', 'Hary Tanoe', 'Hatta Rajasa', 'Jerry Hermawan Lo', 'Kombes Wiliardi Wizard', 'Haryono', 'Enggak Pak', 'Dan', 'Elsa', 'Banyak', 'Ketua Komisi Pemberantasan Korupsi', 'Berdasarkan', 'Cikeas', 'Dewan Gubernur BI Aulia Tantowi Pohan', 'Hotman', 'Lapangan Golf Modernland', 'Agus Harimurti Yudhoyono', 'Wakil Ketua Bidang Pencegahan', 'Hatta', 'Agus', 'Ini', 'Harry Tanoe', 'Tapi Bapak', 'Aulia Pohan', 'Jeffery Lumompow', 'Nasrudin Zulkarnaen', 'Setelah', 'Direktur PT Putra Rajawali Banjaran', 'Rani Juliani', 'Gedung Kementerian Kelautan', 'Nasruddin Zulkarnaen', 'Grand Mahakam', 'Bonyamin Saiman', 'Namun', 'Haryono Umar', 'Tanah Air', 'Direktur PT Rajawali Putra Banjaran Nasrudin Zulkarnaen', 'Ketua', 'Mahkamah Agung', 'Pak Antasari', 'Susilo Bambang Yudhoyono', 'Besan', 'Ketua KPK', 'Nasrudin', 'Allah', 'Menurut', 'Antasari Azhar', 'Yang', 'Pilkada DKI Jakarta', 'Sigit Haryo Wibisono', 'Ketua Umum Partai Perindo', 'Ibas', 'Jakarta Pusat', 'Perikanan', 'Bareskrim', 'Hotman Paris Hutapea', 'Yayasan Pengembangan Perbankan'], ['Edi Baskoro Yudhoyono', 'Susilo Bambang Yudhoyono', 'Antasari', 'Antara SBY', 'Bantah Pernyataan Antasari Azhar', 'Dikutip', 'Mabes Polri', 'Antasari Azhar', 'Cikeas', 'Dengan', 'Partai Demokrat', 'Agus Harimurti Yudhoyono', 'Aulia Pohan', 'Putra Rajawali Banjaran', 'Pilkada DKI', 'Nasrudin Zulkarnaen', 'Selasa'], ['Rabu', 'Direktur Utama PT Putra Rajawali Banjaran', 'Syafril Nasution', 'Antasari', 'Perikanan', 'Pilkada', 'Deputi Gubernur Bank Indonesia', 'Selasa', 'Usai', 'Aslim Tadjuddin', 'Ahok', 'Yayasan Lembaga Pengembangan Perbankan', 'Sylviana Murni', 'Gedung KKP', 'Strategi Pilkada', 'Ketua Komisi Pemberantasan Korupsi', 'Cikeas', 'Pengadilan Tindak Pidana Korupsi', 'Gubernur DKI', 'Jokowi', 'Ketua KPK Antasari Azhar', 'Aulia Pohan', 'Bunbunan Hutapea', 'Jaksa', 'Dia', 'Jambore Mahasiswa', 'Gedung Kementerian Kelautan', 'Nasruddin Zulkarnaen', 'Benarkah Istana', 'Presiden Joko Jokowi Widodo', 'Hary Tanoesudibjo JAKARTA', 'Susilo Bambang Yudhoyono', 'Agus Harimurti', 'Mahkamah Agung', 'Bareskrim Mabes Polri', 'Hary Tanoesudibjo', 'Orang', 'Aulia', 'Antasari Azhar', 'Sementara', 'Saya', 'Ketua Partai Perindo', 'Kepala Kejaksaan Negeri Jakarta Selatan']]

graph = []
label = {}
temp = {}
for item in entity:
    for i in item:
        for j in item:
            if i != j:
                val = (i, j)
                if val in temp:
                    temp[val] = temp[val] + 1
                    if temp[val] > 1:
                        label[val] = temp[val]
                        graph.append(val)
                else:
                    temp[val] = 1

draw_graph(graph, label)

