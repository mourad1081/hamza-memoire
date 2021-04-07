# Generated by Django 3.1.7 on 2021-04-05 10:21
from random import randint, choice

from django.db import migrations

affiliations = [
	{"name": "Euismod Inc."},
	{"name": "Tristique Neque Venenatis Corporation"},
	{"name": "Nulla Associates"},
	{"name": "Vitae Posuere Foundation"},
	{"name": "Facilisis Corporation"},
	{"name": "Augue Eu Corp."},
	{"name": "Luctus Industries"},
	{"name": "Cursus Et Corporation"},
	{"name": "Laoreet Posuere Enim Ltd"},
	{"name": "Semper Tellus Id Associates"},
	{"name": "Ipsum Associates"},
	{"name": "Eu Accumsan Sed LLP"},
	{"name": "Felis Orci Corporation"},
	{"name": "Ornare LLP"},
	{"name": "Rutrum Associates"},
	{"name": "Nunc Ac Ltd"},
	{"name": "Dolor Corp."},
	{"name": "Quis Arcu Vel Associates"},
	{"name": "Donec Inc."},
	{"name": "Mollis Duis Sit Institute"},
	{"name": "Vitae Sodales Nisi Associates"},
	{"name": "Tincidunt Nibh Associates"},
	{"name": "Ac Mattis Ornare Incorporated"},
	{"name": "Tortor Nibh Corporation"},
	{"name": "Bibendum Sed Est Foundation"},
	{"name": "Ullamcorper LLP"},
	{"name": "Sapien PC"},
	{"name": "A Felis Ullamcorper Inc."},
	{"name": "Vel Nisl Industries"},
	{"name": "In Cursus Industries"},
	{"name": "Mi Institute"},
	{"name": "Dictum Consulting"},
	{"name": "Tellus Justo Sit Corporation"},
	{"name": "Placerat Corporation"},
	{"name": "Accumsan Laoreet Industries"},
	{"name": "Suspendisse Commodo Incorporated"},
	{"name": "Erat Neque Company"},
	{"name": "Parturient Montes Nascetur Incorporated"},
	{"name": "Quis Urna Nunc Company"},
	{"name": "Iaculis Quis LLC"},
	{"name": "Tristique Institute"},
	{"name": "Dui Quis LLP"},
	{"name": "Quisque PC"},
	{"name": "Maecenas Mi Ltd"},
	{"name": "Ut Consulting"},
	{"name": "Dui In Institute"},
	{"name": "Rhoncus Nullam Velit Associates"},
	{"name": "Et Corp."},
	{"name": "Iaculis Quis Pede Incorporated"},
	{"name": "Dapibus Id Industries"},
	{"name": "Consequat Dolor Corporation"},
	{"name": "Sapien Cras Ltd"},
	{"name": "Viverra Ltd"},
	{"name": "Integer Corporation"},
	{"name": "Fringilla Ltd"},
	{"name": "Mi Eleifend Egestas LLP"},
	{"name": "Ut Aliquam Iaculis Corp."},
	{"name": "Pharetra Ut Pharetra PC"},
	{"name": "Quis Pede Industries"},
	{"name": "Tristique Institute"},
	{"name": "Duis Gravida Praesent Ltd"},
	{"name": "Blandit Company"},
	{"name": "In Faucibus Orci Incorporated"},
	{"name": "Purus Ac Tellus LLP"},
	{"name": "Cursus Et Magna LLP"},
	{"name": "In Institute"},
	{"name": "Libero Donec Limited"},
	{"name": "Aliquam Arcu Aliquam Company"},
	{"name": "Ultrices Sit Consulting"},
	{"name": "Augue Id Ante Incorporated"},
	{"name": "Fermentum Fermentum Limited"},
	{"name": "Fermentum Associates"},
	{"name": "Tempor Ltd"},
	{"name": "Eget Limited"},
	{"name": "Ut Semper Pretium Corp."},
	{"name": "Et Pede LLC"},
	{"name": "Morbi Accumsan Laoreet Corporation"},
	{"name": "Sem Vitae Corp."},
	{"name": "Justo Faucibus Inc."},
	{"name": "In Faucibus LLP"},
	{"name": "Mus Ltd"},
	{"name": "Lectus Pede Ultrices Corp."},
	{"name": "Pharetra Nam Ac Consulting"},
	{"name": "Nec Ante Maecenas Consulting"},
	{"name": "Ligula Tortor Dictum Inc."},
	{"name": "Aliquet Nec Imperdiet Inc."},
	{"name": "Metus Aenean Foundation"},
	{"name": "Iaculis Limited"},
	{"name": "Tristique Inc."},
	{"name": "Sollicitudin Corp."},
	{"name": "Augue Ac Institute"},
	{"name": "Cras Associates"},
	{"name": "Commodo Tincidunt Nibh Ltd"},
	{"name": "Urna Nullam Lobortis Associates"},
	{"name": "Lorem Semper Auctor Incorporated"},
	{"name": "Nunc Id Enim Foundation"},
	{"name": "Pellentesque Incorporated"},
	{"name": "In Scelerisque Ltd"},
	{"name": "Nunc Incorporated"},
	{"name": "Magna Lorem PC"},
	{"name": "Cras Interdum Company"},
	{"name": "Maecenas Associates"},
	{"name": "Ut Aliquam Iaculis Limited"},
	{"name": "Mauris Id Corp."},
	{"name": "Ac Urna Ut Consulting"},
	{"name": "Risus Varius Limited"},
	{"name": "Congue Elit Limited"},
	{"name": "Et Pede Nunc LLP"},
	{"name": "Orci Lacus Consulting"},
	{"name": "Donec Egestas Incorporated"},
	{"name": "Magna Corp."},
	{"name": "Pellentesque Habitant Morbi PC"},
	{"name": "Sed Dictum Eleifend PC"},
	{"name": "Non LLC"},
	{"name": "Ac Company"},
	{"name": "Ligula Aenean Euismod LLC"},
	{"name": "Erat Eget Tincidunt Industries"},
	{"name": "Volutpat Nunc Industries"},
	{"name": "Risus Corporation"},
	{"name": "Sed Leo Foundation"},
	{"name": "Leo Cras Foundation"},
	{"name": "In Institute"},
	{"name": "Ipsum Nunc Inc."},
	{"name": "Sodales Purus Associates"},
	{"name": "Aliquam Corporation"},
	{"name": "Lorem Ipsum Foundation"},
	{"name": "Neque Institute"},
	{"name": "Phasellus Inc."},
	{"name": "Non Cursus Non Foundation"},
	{"name": "Orci Lacus Vestibulum Incorporated"},
	{"name": "Porttitor Interdum LLC"},
	{"name": "Vitae Mauris Sit Ltd"},
	{"name": "Blandit Nam Nulla Ltd"},
	{"name": "At Nisi Institute"},
	{"name": "Donec Tincidunt Consulting"},
	{"name": "Cras Consulting"},
	{"name": "Eu Tellus Industries"},
	{"name": "Nunc Limited"},
	{"name": "Ligula Consulting"},
	{"name": "Eu Corp."},
	{"name": "Cursus Nunc Corp."},
	{"name": "Ullamcorper Viverra Inc."},
	{"name": "Quisque Ac LLC"},
	{"name": "Quis Limited"},
	{"name": "Ipsum Industries"},
	{"name": "Morbi Quis Corp."},
	{"name": "Magnis Dis Parturient Consulting"},
	{"name": "Et Magna LLP"},
	{"name": "Eget Metus Ltd"},
	{"name": "Mi Company"},
	{"name": "Magna Institute"},
	{"name": "Nibh Aliquam Corporation"},
	{"name": "Curabitur Foundation"},
	{"name": "Nibh Limited"},
	{"name": "Lacus Aliquam Rutrum Company"},
	{"name": "Neque Pellentesque Massa Limited"},
	{"name": "Praesent Interdum Ligula LLP"},
	{"name": "Turpis Vitae Consulting"},
	{"name": "Purus LLP"},
	{"name": "Velit Sed Malesuada Limited"},
	{"name": "Iaculis Nec LLP"},
	{"name": "Amet Diam Eu Limited"},
	{"name": "Luctus Curabitur Inc."},
	{"name": "Est Mollis Ltd"},
	{"name": "Dapibus Id Consulting"},
	{"name": "Mollis Vitae Posuere LLC"},
	{"name": "Aliquet Proin Velit LLP"},
	{"name": "Commodo Hendrerit Donec Company"},
	{"name": "Quis Massa Mauris Corp."},
	{"name": "Non Massa Non LLC"},
	{"name": "Mollis Corp."},
	{"name": "Convallis Est Vitae Institute"},
	{"name": "Ipsum Suspendisse Non Limited"},
	{"name": "Ipsum Sodales Purus Inc."},
	{"name": "Sapien Nunc Pulvinar Industries"},
	{"name": "Velit Quisque Varius LLP"},
	{"name": "Ac PC"},
	{"name": "Primis In Faucibus Incorporated"},
	{"name": "Ut Consulting"},
	{"name": "Quis Diam Pellentesque Inc."},
	{"name": "Suspendisse Aliquet Molestie Consulting"},
	{"name": "Sed Dolor Fusce Corp."},
	{"name": "Sem Magna LLP"},
	{"name": "Quis Lectus Nullam Institute"},
	{"name": "Purus Nullam Scelerisque Company"},
	{"name": "Lorem Lorem Luctus LLC"},
	{"name": "Interdum Libero Company"},
	{"name": "Sed Eget LLP"},
	{"name": "Augue Porttitor Interdum Corp."},
	{"name": "Orci Adipiscing Non Institute"},
	{"name": "Sit Amet Massa Industries"},
	{"name": "Fringilla Donec Feugiat Ltd"},
	{"name": "Id Incorporated"},
	{"name": "Vestibulum Neque Sed PC"},
	{"name": "Elit Consulting"},
	{"name": "Cras Interdum LLP"},
	{"name": "Dolor Company"},
	{"name": "Sed Nulla Ante Consulting"},
	{"name": "Nec Ligula Corporation"},
	{"name": "Elit Sed Associates"}
]

journals = [
	{"name": "Lectus Limited"},
	{"name": "Egestas Incorporated"},
	{"name": "Felis Orci Adipiscing PC"},
	{"name": "Eu Associates"},
	{"name": "Nunc Lectus Pede Institute"},
	{"name": "Dolor Fusce Mi Ltd"},
	{"name": "Orci Adipiscing Corp."},
	{"name": "Amet Foundation"},
	{"name": "Penatibus Et Magnis PC"},
	{"name": "Auctor Velit LLC"},
	{"name": "Ligula Aenean Consulting"},
	{"name": "Integer Tincidunt Aliquam LLP"},
	{"name": "Sed Industries"},
	{"name": "Non Quam Pellentesque Ltd"},
	{"name": "Velit Egestas Lacinia Consulting"},
	{"name": "Orci Lacus Inc."},
	{"name": "Dis Parturient Montes LLC"},
	{"name": "Massa Corp."},
	{"name": "Erat LLC"},
	{"name": "Quis Diam Limited"},
	{"name": "Amet Metus Aliquam Limited"},
	{"name": "Hendrerit Id Ante PC"},
	{"name": "Sed Foundation"},
	{"name": "Diam Nunc Ullamcorper Associates"},
	{"name": "Dolor Institute"},
	{"name": "Morbi Sit Institute"},
	{"name": "Est Ac Mattis LLC"},
	{"name": "Et Ultrices LLP"},
	{"name": "Leo In Inc."},
	{"name": "Ac Turpis LLC"},
	{"name": "Dictum Corp."},
	{"name": "Rutrum Fusce Corporation"},
	{"name": "Aliquam Fringilla Industries"},
	{"name": "Quisque Consulting"},
	{"name": "Quis Pede PC"},
	{"name": "Aliquet Sem Ut Limited"},
	{"name": "Suspendisse Sagittis Institute"},
	{"name": "Metus Facilisis Lorem Incorporated"},
	{"name": "Tincidunt Orci Quis Ltd"},
	{"name": "Magna Suspendisse Corporation"},
	{"name": "Donec Incorporated"},
	{"name": "Orci Luctus Et Industries"},
	{"name": "Lectus Consulting"},
	{"name": "Consequat Corporation"},
	{"name": "Ipsum Inc."},
	{"name": "Ipsum Associates"},
	{"name": "Nunc Corporation"},
	{"name": "Fringilla Est Mauris Institute"},
	{"name": "Imperdiet LLP"},
	{"name": "Placerat Inc."},
	{"name": "Erat Etiam Corporation"},
	{"name": "Sit Amet Incorporated"},
	{"name": "Vel Est LLP"},
	{"name": "Dignissim Magna A Corp."},
	{"name": "Gravida Mauris PC"},
	{"name": "Nisi Mauris Corp."},
	{"name": "Dolor Quam Elementum Consulting"},
	{"name": "Nisi Nibh Lacinia Institute"},
	{"name": "Elit Institute"},
	{"name": "Nisl Arcu Iaculis Institute"},
	{"name": "Eleifend Cras Sed Associates"},
	{"name": "Turpis Nulla Aliquet Consulting"},
	{"name": "Ac Metus Vitae Institute"},
	{"name": "Elit Pede PC"},
	{"name": "Nostra Company"},
	{"name": "Mi Lacinia Mattis PC"},
	{"name": "Posuere Vulputate Lacus LLC"},
	{"name": "Nonummy Ultricies Incorporated"},
	{"name": "Euismod Inc."},
	{"name": "Tempor Lorem Eget Corporation"},
	{"name": "Ultrices Corporation"},
	{"name": "Cras Interdum Industries"},
	{"name": "Eu Incorporated"},
	{"name": "Nunc Est Mollis Corporation"},
	{"name": "Ornare Industries"},
	{"name": "Donec Nibh Consulting"},
	{"name": "Nulla Integer Inc."},
	{"name": "Arcu Foundation"},
	{"name": "Ornare Company"},
	{"name": "Sem Eget Massa Consulting"},
	{"name": "Phasellus At Augue Associates"},
	{"name": "Metus Aliquam Erat Limited"},
	{"name": "Gravida Praesent Eu Corp."},
	{"name": "Diam Pellentesque Limited"},
	{"name": "Nec Orci Inc."},
	{"name": "Libero Nec Ligula Associates"},
	{"name": "Penatibus Ltd"},
	{"name": "Suspendisse Aliquet Industries"},
	{"name": "Dolor Vitae Dolor Company"},
	{"name": "Tincidunt Tempus Risus LLC"},
	{"name": "Lectus Associates"},
	{"name": "Libero Incorporated"},
	{"name": "Ac Industries"},
	{"name": "Lorem Ut Aliquam Corporation"},
	{"name": "Amet Faucibus Ut Company"},
	{"name": "Aliquet Company"},
	{"name": "Diam Proin Dolor LLC"},
	{"name": "Ut Nec Urna LLP"},
	{"name": "Nisi A Odio PC"},
	{"name": "Sociis Incorporated"}
]

authors = [
	{"first_name": "Eden", "last_name": "Kennedy", "email": "molestie.orci.tincidunt@diamvelarcu.net", "affiliation_id": 15, "country_id": 33},
	{"first_name": "Aspen", "last_name": "Nguyen", "email": "montes.nascetur.ridiculus@congueelit.net", "affiliation_id": 98, "country_id": 4},
	{"first_name": "Dawn", "last_name": "Cohen", "email": "mus.Donec@atortorNunc.co.uk", "affiliation_id": 74, "country_id": 39},
	{"first_name": "Rana", "last_name": "Mathews", "email": "diam.Pellentesque@vehicularisus.net", "affiliation_id": 28, "country_id": 6},
	{"first_name": "Allen", "last_name": "Harrell", "email": "sagittis.semper@variuset.com", "affiliation_id": 77, "country_id": 12},
	{"first_name": "Arsenio", "last_name": "Sanchez", "email": "pretium@enimMaurisquis.co.uk", "affiliation_id": 48, "country_id": 24},
	{"first_name": "Lynn", "last_name": "Ortega", "email": "eu@vulputate.edu", "affiliation_id": 78, "country_id": 12},
	{"first_name": "Yeo", "last_name": "Atkinson", "email": "metus.sit@estmollis.ca", "affiliation_id": 32, "country_id": 26},
	{"first_name": "Madison", "last_name": "Shepherd", "email": "lorem@infelis.net", "affiliation_id": 7, "country_id": 28},
	{"first_name": "Rebekah", "last_name": "Barrett", "email": "Pellentesque@nuncinterdumfeugiat.com", "affiliation_id": 43, "country_id": 42},
	{"first_name": "Hanae", "last_name": "Hart", "email": "eleifend.non.dapibus@rutrumjusto.org", "affiliation_id": 13, "country_id": 26},
	{"first_name": "Mallory", "last_name": "Dillard", "email": "ultricies.ornare.elit@eliteratvitae.org", "affiliation_id": 90, "country_id": 2},
	{"first_name": "Medge", "last_name": "Koch", "email": "massa.non@lectusCum.net", "affiliation_id": 22, "country_id": 12},
	{"first_name": "Illiana", "last_name": "Spencer", "email": "vulputate.mauris.sagittis@ametorciUt.co.uk", "affiliation_id": 99, "country_id": 8},
	{"first_name": "Kareem", "last_name": "Bean", "email": "dui.in.sodales@turpisnecmauris.edu", "affiliation_id": 40, "country_id": 26},
	{"first_name": "Virginia", "last_name": "Barron", "email": "malesuada@duiquisaccumsan.com", "affiliation_id": 43, "country_id": 10},
	{"first_name": "Edward", "last_name": "Hoover", "email": "consectetuer.adipiscing.elit@pellentesque.ca", "affiliation_id": 80, "country_id": 16},
	{"first_name": "Jarrod", "last_name": "Terrell", "email": "Maecenas.mi@Aeneanegetmagna.edu", "affiliation_id": 68, "country_id": 20},
	{"first_name": "Nissim", "last_name": "Crawford", "email": "nonummy@sedturpisnec.edu", "affiliation_id": 64, "country_id": 38},
	{"first_name": "Clinton", "last_name": "Chang", "email": "ornare@enimdiamvel.co.uk", "affiliation_id": 76, "country_id": 26},
	{"first_name": "Drake", "last_name": "Herman", "email": "ornare.elit@erategetipsum.co.uk", "affiliation_id": 82, "country_id": 36},
	{"first_name": "Murphy", "last_name": "Rowland", "email": "tortor.at@risus.ca", "affiliation_id": 85, "country_id": 30},
	{"first_name": "Akeem", "last_name": "Hudson", "email": "nonummy@penatibuset.net", "affiliation_id": 62, "country_id": 8},
	{"first_name": "Joan", "last_name": "Whitley", "email": "non.enim@elementum.edu", "affiliation_id": 31, "country_id": 36},
	{"first_name": "Geraldine", "last_name": "Kennedy", "email": "dui@apurus.ca", "affiliation_id": 77, "country_id": 26},
	{"first_name": "Mariko", "last_name": "Rios", "email": "molestie.sodales@pretiumet.com", "affiliation_id": 24, "country_id": 18},
	{"first_name": "Jackson", "last_name": "Huff", "email": "lorem.auctor.quis@Integermollis.edu", "affiliation_id": 11, "country_id": 31},
	{"first_name": "Madeline", "last_name": "Phelps", "email": "diam@placeratorcilacus.net", "affiliation_id": 14, "country_id": 18},
	{"first_name": "Daria", "last_name": "Mayo", "email": "rutrum.justo@et.ca", "affiliation_id": 39, "country_id": 15},
	{"first_name": "Yvonne", "last_name": "Ayers", "email": "non.lorem.vitae@augueSed.org", "affiliation_id": 67, "country_id": 34},
	{"first_name": "Martin", "last_name": "Benson", "email": "nunc@dolor.co.uk", "affiliation_id": 78, "country_id": 44},
	{"first_name": "Kieran", "last_name": "Franks", "email": "nunc@urnaUt.com", "affiliation_id": 19, "country_id": 37},
	{"first_name": "Graham", "last_name": "Bridges", "email": "vehicula.et.rutrum@egestasa.org", "affiliation_id": 80, "country_id": 35},
	{"first_name": "Alice", "last_name": "Whitfield", "email": "Duis.a.mi@semut.org", "affiliation_id": 73, "country_id": 2},
	{"first_name": "Nathaniel", "last_name": "Whitfield", "email": "diam.Proin.dolor@laciniaatiaculis.edu", "affiliation_id": 94, "country_id": 48},
	{"first_name": "Oprah", "last_name": "Alvarez", "email": "Fusce@eget.co.uk", "affiliation_id": 48, "country_id": 8},
	{"first_name": "Rhiannon", "last_name": "Jackson", "email": "sagittis.lobortis@lectus.net", "affiliation_id": 95, "country_id": 31},
	{"first_name": "Charissa", "last_name": "Reid", "email": "Nulla@mauris.ca", "affiliation_id": 79, "country_id": 3},
	{"first_name": "Kameko", "last_name": "Ruiz", "email": "ornare.placerat.orci@sagittisNullamvitae.org", "affiliation_id": 89, "country_id": 23},
	{"first_name": "Karly", "last_name": "Fernandez", "email": "lorem@tortorIntegeraliquam.net", "affiliation_id": 77, "country_id": 20},
	{"first_name": "Lisandra", "last_name": "Ford", "email": "quis.accumsan@ultricesmauris.net", "affiliation_id": 68, "country_id": 18},
	{"first_name": "Anne", "last_name": "Powell", "email": "Nullam.scelerisque@dignissim.com", "affiliation_id": 25, "country_id": 38},
	{"first_name": "TaShya", "last_name": "Yang", "email": "commodo.ipsum.Suspendisse@interdumCurabitur.ca", "affiliation_id": 16, "country_id": 30},
	{"first_name": "Cullen", "last_name": "Turner", "email": "sit.amet@eget.co.uk", "affiliation_id": 77, "country_id": 44},
	{"first_name": "Ryder", "last_name": "Knight", "email": "Nulla.aliquet@nonmassa.co.uk", "affiliation_id": 96, "country_id": 26},
	{"first_name": "Mariko", "last_name": "Bennett", "email": "facilisis@augueutlacus.ca", "affiliation_id": 47, "country_id": 39},
	{"first_name": "Drew", "last_name": "Stone", "email": "vel@temporarcu.com", "affiliation_id": 84, "country_id": 46},
	{"first_name": "Portia", "last_name": "Bradshaw", "email": "pharetra@arcuimperdietullamcorper.ca", "affiliation_id": 93, "country_id": 49},
	{"first_name": "Rudyard", "last_name": "Bentley", "email": "dui.in.sodales@Nullaeget.org", "affiliation_id": 56, "country_id": 16},
	{"first_name": "Len", "last_name": "Pittman", "email": "tempus@semegestas.com", "affiliation_id": 16, "country_id": 26},
	{"first_name": "Lucian", "last_name": "Moody", "email": "eget.dictum@aliquameros.com", "affiliation_id": 22, "country_id": 1},
	{"first_name": "Lillian", "last_name": "Parks", "email": "pede.Praesent.eu@nuncid.net", "affiliation_id": 35, "country_id": 42},
	{"first_name": "Reece", "last_name": "Cobb", "email": "Aenean@felispurusac.com", "affiliation_id": 87, "country_id": 24},
	{"first_name": "Kirsten", "last_name": "Fox", "email": "libero@faucibusleoin.net", "affiliation_id": 76, "country_id": 22},
	{"first_name": "Amity", "last_name": "Bowen", "email": "purus@conubianostraper.org", "affiliation_id": 40, "country_id": 22},
	{"first_name": "Branden", "last_name": "Terry", "email": "eu.nibh.vulputate@etmagnisdis.org", "affiliation_id": 8, "country_id": 6},
	{"first_name": "Craig", "last_name": "Harper", "email": "sed@Maurisblandit.com", "affiliation_id": 85, "country_id": 41},
	{"first_name": "Stuart", "last_name": "Ramirez", "email": "ipsum.Suspendisse.sagittis@tempusnonlacinia.com", "affiliation_id": 81, "country_id": 24},
	{"first_name": "Guinevere", "last_name": "Avery", "email": "pede.et.risus@sem.ca", "affiliation_id": 26, "country_id": 7},
	{"first_name": "Vladimir", "last_name": "Rivas", "email": "Nunc.sed@nonante.edu", "affiliation_id": 35, "country_id": 35},
	{"first_name": "Philip", "last_name": "Vasquez", "email": "Etiam.ligula@fringillapurus.net", "affiliation_id": 11, "country_id": 50},
	{"first_name": "Rosalyn", "last_name": "Watkins", "email": "tempor.lorem@magna.ca", "affiliation_id": 11, "country_id": 12},
	{"first_name": "Keely", "last_name": "Cox", "email": "sed.est.Nunc@eteuismodet.net", "affiliation_id": 47, "country_id": 48},
	{"first_name": "Carol", "last_name": "Mckay", "email": "feugiat.tellus@SuspendissesagittisNullam.ca", "affiliation_id": 42, "country_id": 35},
	{"first_name": "Zeph", "last_name": "Floyd", "email": "venenatis.vel.faucibus@tempus.co.uk", "affiliation_id": 27, "country_id": 27},
	{"first_name": "Grant", "last_name": "Guthrie", "email": "aliquet@nequeseddictum.com", "affiliation_id": 39, "country_id": 39},
	{"first_name": "Jorden", "last_name": "Mills", "email": "eget@Donec.ca", "affiliation_id": 33, "country_id": 25},
	{"first_name": "Courtney", "last_name": "Larson", "email": "ipsum@porttitorvulputateposuere.net", "affiliation_id": 66, "country_id": 1},
	{"first_name": "Tiger", "last_name": "Petersen", "email": "hendrerit@aliquam.net", "affiliation_id": 8, "country_id": 32},
	{"first_name": "Elvis", "last_name": "Potter", "email": "risus.odio@mus.org", "affiliation_id": 81, "country_id": 16},
	{"first_name": "Keaton", "last_name": "Graves", "email": "malesuada.vel@consequatenim.ca", "affiliation_id": 25, "country_id": 6},
	{"first_name": "Charlotte", "last_name": "Miles", "email": "rutrum.Fusce@Aliquamgravida.co.uk", "affiliation_id": 9, "country_id": 26},
	{"first_name": "Armando", "last_name": "Willis", "email": "sociis.natoque@elitelit.org", "affiliation_id": 99, "country_id": 38},
	{"first_name": "Arthur", "last_name": "Forbes", "email": "elit.elit@nonluctussit.net", "affiliation_id": 65, "country_id": 31},
	{"first_name": "Finn", "last_name": "Rowland", "email": "ultrices.posuere.cubilia@Nam.edu", "affiliation_id": 12, "country_id": 50},
	{"first_name": "Edan", "last_name": "Craft", "email": "senectus.et.netus@massa.com", "affiliation_id": 88, "country_id": 31},
	{"first_name": "Adele", "last_name": "Leblanc", "email": "eget.tincidunt.dui@lacusMauris.com", "affiliation_id": 55, "country_id": 3},
	{"first_name": "Briar", "last_name": "Watkins", "email": "litora@Quisque.co.uk", "affiliation_id": 60, "country_id": 36},
	{"first_name": "Herman", "last_name": "Wong", "email": "magna@gravida.net", "affiliation_id": 29, "country_id": 15},
	{"first_name": "Thane", "last_name": "Guthrie", "email": "lacinia.at.iaculis@diamnuncullamcorper.org", "affiliation_id": 90, "country_id": 6},
	{"first_name": "Inez", "last_name": "Dickson", "email": "auctor@tincidunt.com", "affiliation_id": 73, "country_id": 32},
	{"first_name": "Vivian", "last_name": "Pratt", "email": "nibh.dolor.nonummy@ultricesposuerecubilia.net", "affiliation_id": 94, "country_id": 8},
	{"first_name": "Arden", "last_name": "Harrell", "email": "Sed@Morbi.edu", "affiliation_id": 29, "country_id": 6},
	{"first_name": "Alexis", "last_name": "Hebert", "email": "ac.feugiat@mollisInteger.net", "affiliation_id": 74, "country_id": 9},
	{"first_name": "Ella", "last_name": "Bauer", "email": "sem.ut@consectetuermauris.net", "affiliation_id": 58, "country_id": 7},
	{"first_name": "Lester", "last_name": "Henderson", "email": "at.nisi@aliquamarcu.ca", "affiliation_id": 18, "country_id": 33},
	{"first_name": "Andrew", "last_name": "Mercer", "email": "dolor.dolor@iaculisenimsit.net", "affiliation_id": 52, "country_id": 46},
	{"first_name": "Steel", "last_name": "Silva", "email": "sagittis.Nullam.vitae@ipsumCurabitur.ca", "affiliation_id": 41, "country_id": 30},
	{"first_name": "Elmo", "last_name": "Wiley", "email": "mi.lacinia@purussapien.co.uk", "affiliation_id": 47, "country_id": 9},
	{"first_name": "Jade", "last_name": "Lang", "email": "eu.tempor@convallis.net", "affiliation_id": 56, "country_id": 39},
	{"first_name": "Cadman", "last_name": "Winters", "email": "porttitor.tellus.non@Duiscursus.edu", "affiliation_id": 4, "country_id": 38},
	{"first_name": "Orson", "last_name": "Mercado", "email": "Donec.tempor.est@acmi.edu", "affiliation_id": 50, "country_id": 7},
	{"first_name": "Christine", "last_name": "Michael", "email": "sed.pede.nec@ad.net", "affiliation_id": 94, "country_id": 40},
	{"first_name": "Matthew", "last_name": "Horton", "email": "tellus@egetmetus.org", "affiliation_id": 38, "country_id": 1},
	{"first_name": "Justina", "last_name": "Cooley", "email": "libero@nuncullamcorper.org", "affiliation_id": 53, "country_id": 4},
	{"first_name": "Lance", "last_name": "Jimenez", "email": "vitae@velquamdignissim.co.uk", "affiliation_id": 72, "country_id": 40},
	{"first_name": "Dale", "last_name": "Flynn", "email": "In.nec@Fuscemollis.ca", "affiliation_id": 77, "country_id": 16},
	{"first_name": "Geraldine", "last_name": "Morris", "email": "arcu.imperdiet.ullamcorper@nibhAliquam.co.uk", "affiliation_id": 33, "country_id": 50},
	{"first_name": "Otto", "last_name": "Mcgowan", "email": "Cras.interdum.Nunc@Donecfringilla.com", "affiliation_id": 96, "country_id": 21},
	{"first_name": "Fulton", "last_name": "Atkinson", "email": "Fusce@enimnonnisi.com", "affiliation_id": 86, "country_id": 47}
]

references = [
	{"year": 2010, "title": "augue id ante dictum cursus. Nunc mauris", "pages": 401, "volume": 90, "journal_id": 52},
	{"year": 2010, "title": "a purus. Duis elementum,", "pages": 315, "volume": 5, "journal_id": 47},
	{"year": 2015, "title": "ornare", "pages": 621, "volume": 94, "journal_id": 87},
	{"year": 2008, "title": "et magnis dis parturient montes, nascetur ridiculus mus. Donec dignissim", "pages": 499, "volume": 39, "journal_id": 18},
	{"year": 2020, "title": "convallis ligula. Donec", "pages": 587, "volume": 92, "journal_id": 72},
	{"year": 1949, "title": "rutrum. Fusce dolor quam, elementum at, egestas a, scelerisque sed,", "pages": 897, "volume": 11, "journal_id": 51},
	{"year": 2000, "title": "nec ante. Maecenas mi felis, adipiscing fringilla,", "pages": 700, "volume": 94, "journal_id": 45},
	{"year": 1956, "title": "pellentesque, tellus sem mollis dui, in", "pages": 381, "volume": 3, "journal_id": 57},
	{"year": 2018, "title": "Nunc laoreet lectus quis massa. Mauris vestibulum, neque", "pages": 472, "volume": 16, "journal_id": 82},
	{"year": 1973, "title": "dictum mi, ac mattis velit justo", "pages": 682, "volume": 40, "journal_id": 3},
	{"year": 1945, "title": "et tristique pellentesque,", "pages": 687, "volume": 97, "journal_id": 15},
	{"year": 1970, "title": "imperdiet nec, leo. Morbi neque tellus, imperdiet non, vestibulum nec,", "pages": 645, "volume": 57, "journal_id": 23},
	{"year": 1990, "title": "Nunc sed orci lobortis augue scelerisque mollis. Phasellus libero mauris,", "pages": 90, "volume": 70, "journal_id": 15},
	{"year": 2015, "title": "elementum,", "pages": 925, "volume": 60, "journal_id": 80},
	{"year": 1981, "title": "tristique ac, eleifend vitae, erat. Vivamus", "pages": 971, "volume": 50, "journal_id": 21},
	{"year": 2012, "title": "Nunc sollicitudin commodo ipsum. Suspendisse non leo.", "pages": 379, "volume": 41, "journal_id": 54},
	{"year": 2012, "title": "nisi nibh lacinia orci, consectetuer euismod est", "pages": 206, "volume": 84, "journal_id": 56},
	{"year": 2012, "title": "libero", "pages": 264, "volume": 32, "journal_id": 71},
	{"year": 1948, "title": "tempus mauris", "pages": 192, "volume": 34, "journal_id": 77},
	{"year": 1990, "title": "Vestibulum ut eros non enim commodo", "pages": 529, "volume": 64, "journal_id": 80},
	{"year": 1996, "title": "libero", "pages": 675, "volume": 70, "journal_id": 50},
	{"year": 2004, "title": "neque non", "pages": 61, "volume": 8, "journal_id": 41},
	{"year": 1996, "title": "Donec est.", "pages": 964, "volume": 11, "journal_id": 40},
	{"year": 1976, "title": "aliquam adipiscing lacus. Ut nec urna", "pages": 668, "volume": 90, "journal_id": 59},
	{"year": 2015, "title": "imperdiet nec, leo.", "pages": 217, "volume": 6, "journal_id": 37},
	{"year": 1971, "title": "Cras sed leo. Cras vehicula", "pages": 104, "volume": 42, "journal_id": 73},
	{"year": 1943, "title": "Fusce fermentum fermentum arcu. Vestibulum ante ipsum", "pages": 217, "volume": 85, "journal_id": 2},
	{"year": 1972, "title": "elit. Nulla", "pages": 884, "volume": 2, "journal_id": 56},
	{"year": 2011, "title": "est. Nunc ullamcorper, velit", "pages": 789, "volume": 29, "journal_id": 59},
	{"year": 1987, "title": "lacus. Aliquam rutrum lorem", "pages": 719, "volume": 71, "journal_id": 73},
	{"year": 1943, "title": "adipiscing elit. Etiam laoreet,", "pages": 16, "volume": 61, "journal_id": 74},
	{"year": 1967, "title": "posuere, enim nisl elementum purus, accumsan interdum libero dui nec", "pages": 461, "volume": 32, "journal_id": 9},
	{"year": 1993, "title": "orci luctus et ultrices posuere cubilia", "pages": 941, "volume": 27, "journal_id": 11},
	{"year": 2002, "title": "adipiscing lobortis risus. In mi pede, nonummy", "pages": 159, "volume": 93, "journal_id": 75},
	{"year": 1972, "title": "odio. Phasellus at augue id", "pages": 543, "volume": 45, "journal_id": 84},
	{"year": 2011, "title": "Nunc mauris elit, dictum eu,", "pages": 955, "volume": 68, "journal_id": 20},
	{"year": 1980, "title": "Donec egestas. Aliquam nec enim. Nunc ut erat.", "pages": 435, "volume": 9, "journal_id": 10},
	{"year": 1981, "title": "orci. Phasellus dapibus quam quis diam.", "pages": 444, "volume": 91, "journal_id": 68},
	{"year": 1959, "title": "commodo tincidunt nibh.", "pages": 949, "volume": 87, "journal_id": 73},
	{"year": 1986, "title": "urna. Vivamus molestie dapibus ligula. Aliquam", "pages": 973, "volume": 37, "journal_id": 62},
	{"year": 2017, "title": "vestibulum nec, euismod in, dolor. Fusce feugiat. Lorem", "pages": 163, "volume": 67, "journal_id": 78},
	{"year": 1981, "title": "malesuada fames ac turpis", "pages": 227, "volume": 1, "journal_id": 91},
	{"year": 1958, "title": "enim, gravida sit amet, dapibus id, blandit at,", "pages": 149, "volume": 45, "journal_id": 58},
	{"year": 2010, "title": "ridiculus mus. Aenean eget magna. Suspendisse tristique neque", "pages": 442, "volume": 19, "journal_id": 66},
	{"year": 1941, "title": "sociis natoque penatibus et", "pages": 648, "volume": 48, "journal_id": 66},
	{"year": 1947, "title": "lectus. Cum sociis natoque penatibus", "pages": 8, "volume": 22, "journal_id": 14},
	{"year": 1955, "title": "Integer eu lacus. Quisque imperdiet, erat nonummy ultricies ornare, elit", "pages": 153, "volume": 6, "journal_id": 99},
	{"year": 1992, "title": "mus. Proin vel arcu eu", "pages": 909, "volume": 75, "journal_id": 29},
	{"year": 1995, "title": "cursus", "pages": 463, "volume": 2, "journal_id": 59},
	{"year": 1957, "title": "rutrum magna. Cras convallis convallis dolor. Quisque", "pages": 446, "volume": 27, "journal_id": 52},
	{"year": 1963, "title": "consectetuer adipiscing elit. Curabitur sed tortor. Integer aliquam adipiscing", "pages": 322, "volume": 12, "journal_id": 25},
	{"year": 1952, "title": "iaculis aliquet diam. Sed diam lorem, auctor", "pages": 870, "volume": 79, "journal_id": 55},
	{"year": 1965, "title": "ipsum cursus vestibulum.", "pages": 166, "volume": 78, "journal_id": 54},
	{"year": 2000, "title": "eu, ligula. Aenean euismod mauris eu elit. Nulla facilisi. Sed", "pages": 934, "volume": 40, "journal_id": 58},
	{"year": 1989, "title": "mauris.", "pages": 695, "volume": 55, "journal_id": 18},
	{"year": 1952, "title": "molestie dapibus ligula. Aliquam erat volutpat.", "pages": 660, "volume": 31, "journal_id": 21},
	{"year": 2010, "title": "a,", "pages": 857, "volume": 24, "journal_id": 14},
	{"year": 1988, "title": "sit amet, consectetuer adipiscing elit. Aliquam auctor, velit", "pages": 52, "volume": 46, "journal_id": 72},
	{"year": 1986, "title": "dolor sit amet, consectetuer adipiscing elit.", "pages": 952, "volume": 42, "journal_id": 27},
	{"year": 1970, "title": "Phasellus fermentum convallis ligula. Donec luctus aliquet odio. Etiam ligula", "pages": 519, "volume": 43, "journal_id": 4},
	{"year": 2013, "title": "adipiscing elit. Aliquam auctor, velit eget laoreet", "pages": 848, "volume": 41, "journal_id": 83},
	{"year": 1992, "title": "elementum sem, vitae aliquam eros", "pages": 276, "volume": 18, "journal_id": 42},
	{"year": 1953, "title": "eu tellus eu augue porttitor interdum. Sed auctor odio", "pages": 424, "volume": 40, "journal_id": 74},
	{"year": 1951, "title": "rutrum. Fusce dolor", "pages": 463, "volume": 89, "journal_id": 38},
	{"year": 1954, "title": "Phasellus elit pede,", "pages": 939, "volume": 56, "journal_id": 69},
	{"year": 1996, "title": "Quisque varius. Nam porttitor scelerisque neque. Nullam nisl.", "pages": 633, "volume": 38, "journal_id": 93},
	{"year": 1982, "title": "augue porttitor interdum.", "pages": 338, "volume": 11, "journal_id": 63},
	{"year": 2020, "title": "malesuada fringilla est. Mauris eu turpis. Nulla", "pages": 964, "volume": 37, "journal_id": 85},
	{"year": 1997, "title": "penatibus et magnis dis parturient", "pages": 537, "volume": 35, "journal_id": 1},
	{"year": 1951, "title": "risus. Morbi metus. Vivamus", "pages": 821, "volume": 3, "journal_id": 34},
	{"year": 1958, "title": "convallis convallis dolor. Quisque tincidunt pede", "pages": 620, "volume": 76, "journal_id": 17},
	{"year": 1971, "title": "odio. Phasellus at", "pages": 389, "volume": 95, "journal_id": 6},
	{"year": 2012, "title": "vitae erat", "pages": 244, "volume": 90, "journal_id": 99},
	{"year": 1952, "title": "mi lacinia", "pages": 978, "volume": 43, "journal_id": 93},
	{"year": 1967, "title": "Proin mi. Aliquam gravida mauris ut mi. Duis risus", "pages": 535, "volume": 88, "journal_id": 21},
	{"year": 1940, "title": "Cras lorem lorem, luctus", "pages": 129, "volume": 51, "journal_id": 3},
	{"year": 1984, "title": "vestibulum massa rutrum magna. Cras", "pages": 934, "volume": 51, "journal_id": 4},
	{"year": 1942, "title": "interdum feugiat.", "pages": 304, "volume": 66, "journal_id": 70},
	{"year": 1947, "title": "et, rutrum non, hendrerit id, ante. Nunc mauris", "pages": 330, "volume": 21, "journal_id": 50},
	{"year": 2012, "title": "turpis nec mauris blandit mattis. Cras eget nisi", "pages": 435, "volume": 69, "journal_id": 2},
	{"year": 1946, "title": "montes, nascetur ridiculus mus. Proin vel", "pages": 923, "volume": 83, "journal_id": 53},
	{"year": 1951, "title": "turpis vitae purus gravida", "pages": 269, "volume": 40, "journal_id": 5},
	{"year": 1943, "title": "luctus et ultrices posuere", "pages": 630, "volume": 67, "journal_id": 49},
	{"year": 1995, "title": "parturient montes, nascetur ridiculus mus.", "pages": 80, "volume": 45, "journal_id": 94},
	{"year": 1991, "title": "enim, sit", "pages": 544, "volume": 30, "journal_id": 88},
	{"year": 1964, "title": "urna justo", "pages": 676, "volume": 81, "journal_id": 81},
	{"year": 1989, "title": "pellentesque, tellus sem mollis", "pages": 937, "volume": 14, "journal_id": 45},
	{"year": 2018, "title": "at pede. Cras vulputate velit eu sem.", "pages": 175, "volume": 33, "journal_id": 87},
	{"year": 1988, "title": "fames ac turpis egestas. Aliquam fringilla", "pages": 65, "volume": 90, "journal_id": 75},
	{"year": 1955, "title": "amet ante. Vivamus non lorem vitae odio", "pages": 642, "volume": 54, "journal_id": 79},
	{"year": 2010, "title": "consequat, lectus sit amet luctus vulputate,", "pages": 689, "volume": 71, "journal_id": 85},
	{"year": 1990, "title": "sagittis. Duis gravida. Praesent", "pages": 944, "volume": 8, "journal_id": 74},
	{"year": 1965, "title": "orci. Phasellus dapibus quam quis diam. Pellentesque habitant morbi", "pages": 778, "volume": 19, "journal_id": 83},
	{"year": 1989, "title": "aliquam, enim nec tempus scelerisque, lorem ipsum", "pages": 562, "volume": 41, "journal_id": 23},
	{"year": 1962, "title": "lacus. Quisque purus sapien, gravida non,", "pages": 150, "volume": 1, "journal_id": 69},
	{"year": 1941, "title": "et magnis", "pages": 876, "volume": 29, "journal_id": 97},
	{"year": 1984, "title": "erat vitae risus. Duis a mi", "pages": 1, "volume": 84, "journal_id": 74},
	{"year": 2010, "title": "augue malesuada malesuada. Integer id magna", "pages": 681, "volume": 78, "journal_id": 6},
	{"year": 1998, "title": "dui, nec", "pages": 740, "volume": 79, "journal_id": 10},
	{"year": 1966, "title": "orci. Phasellus dapibus quam quis diam. Pellentesque habitant morbi", "pages": 149, "volume": 99, "journal_id": 48}
]

def add_data(apps, schema_editor):
    Country = apps.get_model('memoire', 'Country')
    Journal = apps.get_model('memoire', 'Journal')
    for j in journals:
        Journal.objects.create(name=j['name'])

    Affiliation = apps.get_model('memoire', 'Affiliation')
    for a in affiliations:
        Affiliation.objects.create(name=a['name'])

    Author = apps.get_model('memoire', 'Author')
    cc = Country.objects.all()
    for a in authors:
        Author.objects.create(
            first_name=a['first_name'],
            last_name=a['last_name'],
            email=a['email'],
            country=choice(cc),
            affiliation_id=a['affiliation_id']
        )

    Reference = apps.get_model('memoire', 'reference')
    aa = Author.objects.all()
    for r in references:
        created_reference = Reference.objects.create(
            year=r['year'],
            title=r['title'],
            pages=r['pages'],
            volume=r['volume'],
            journal_id=r['journal_id']
        )
        for a in range(randint(1,5)):
            created_reference.authors.add(choice(aa))

class Migration(migrations.Migration):

    dependencies = [
        ('memoire', '0002_import_data'),
    ]

    operations = [
        migrations.RunPython(add_data, migrations.RunPython.noop),
    ]