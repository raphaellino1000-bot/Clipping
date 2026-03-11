import feedparser
import datetime
import pytz
import html
import os

BR = pytz.timezone("America/Sao_Paulo")
agora = datetime.datetime.now(BR)

FEEDS = {
      "WSJ": [
                "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
                "https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
      ],
      "FT": [
                "https://www.ft.com/rss/home",
                "https://www.ft.com/rss/world",
      ],
      "Reuters": [
                "https://feeds.reuters.com/reuters/topNews",
                "https://feeds.reuters.com/reuters/businessNews",
                "https://feeds.reuters.com/reuters/worldNews",
      ],
      "Bloomberg": [
                "https://feeds.bloomberg.com/politics/news.rss",
                "https://feeds.bloomberg.com/markets/news.rss",
      ],
      "NYT": [
                "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
                "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
      ],
      "TheEconomist": [
                "https://www.economist.com/latest/rss.xml",
                "https://www.economist.com/finance-and-economics/rss.xml",
      ],
      "Guardian": [
                "https://www.theguardian.com/world/rss",
                "https://www.theguardian.com/business/rss",
      ],
      "BBC": [
                "https://feeds.bbci.co.uk/news/world/rss.xml",
                "https://feeds.bbci.co.uk/news/business/rss.xml",
      ],
      "AP": [
                "https://rsshub.app/apnews/topics/world-news",
                "https://rsshub.app/apnews/topics/business",
      ],
      "CNBC": [
                "https://www.cnbc.com/id/100003114/device/rss/rss.html",
                "https://www.cnbc.com/id/10000664/device/rss/rss.html",
      ],
}

JANELA_HORAS = 24
cutoff = agora - datetime.timedelta(hours=JANELA_HORAS)

noticias = []

for veiculo, urls in FEEDS.itiemmpso(r)t: 
f e e d pcaorlseetra
diamsp o=r t[ ]d
a t e t ifmoer
 iumrplo ritn  puyrtlzs
:i
m p o r t   h t mtlr
yi:m
p o r t   o s 

 B R   =f epeydt z=. tfiemeedzpoanres(e"rA.mpearriscea(/uSralo)_
P a u l o " ) 
 a g o r af o=r  deanttertyi mien. dfaeteedt.iemnet.rnioews(:B
R ) 

 F E E D S   =   { 
      t i"tWuSlJo" :=  [h
                        t m l . e s c a p"eh(tetnptsr:y/./gfeete(d"st.iat.ldej".,c o"m"/)r.ssst/rRiSpS(W)o)r
                          l d N e w s . x m l " , 
                                  l i n k  "=h tetnptsr:y/./gfeete(d"sl.ian.kd"j,. c"o#m"/)r
                                  s s / R S S M a r k e t s M a i np.uxbm l=" ,e
n t r y .]g,e
t ( " p u"bFlTi"s:h e[d
_ p a r s e d " )" hotrt pesn:t/r/yw.wgwe.tf(t".ucpodma/tresds_/phaormsee"d,"
) 
              " h t t p s : / / wiwfw .pfutb.:c
              o m / r s s / w o r l d " , 
                       ] ,d
                       t   =   d"aRteeuttiemres."d:a t[e
                       t i m e ( * p u b"[h:t6t]p,s :t/z/ifnefeod=sp.yrtezu.tuetrcs)..caosmt/irmeeuztoenres(/BtRo)p
                       N e w s " , 
                                        " h t t p si:f/ /dfte e>d=s .cruetuotfefr:s
. c o m / r e u t e r s / b u s i n e s s N e w sc"o,l
e t a d a s . a p"phetntdp(s(:d/t/,f eveedisc.urleou,t etrist.ucloom,/ rleiuntke)r)s
/ w o r l d N e wesx"c,e
p t   E x]c,e
p t i o n":B
l o o m b e r g " :   [ 
c o n t i n u e 
" h t t pnso:t/i/cfieaesd.se.xbtleonodm(bceorlge.tcaodma/sp)o
l
intoitcisc/inaesw.ss.orrsts("k,e
y = l a m b d a  "xh:t txp[s0:]/,/ freeevdesr.sbel=oTormubee)r
g
.dcaotma/_msatrrk e=t sa/gnoerwas..srtsrsf"t,i
m e ( " %]d,/
% m   % H":N%YMT""):
 t[o
 t a l   =   l e n"(hntottpisc:i/a/sr)s
 s
 .vneyitciumleoss._cuonmi/csoesr v=i cleiss/tx(mdli/crts.sf/rnoymtk/eWyosr(l[dn.[x1m]l "f,o
 r   n   i n   n o"thitctipass:]/)/)r
 s
 si.tneyntsi_mhetsm.lc o=m /"s"e
 rfvoirc edst/,x mvle/ircsusl/on,y tt/iBtuuslion,e slsi.nxkm li"n, 
 n o t i c]i,a
 s : 
     " T hheoErcao_nsotmri s=t "d:t .[s
     t r f t i m e ( ""%hdt/t%pms :%/H/:w%wMw".)e
     c o n o miitsetn.sc_ohmt/mlla t+e=s tf/'r<slsi. xdmalt"a,-
     v e i c u l o = ""{hvtetipcsu:l/o/}w"w wd.aetcao-ntoimtiuslto.=c"o{mt/iftiunlaon.cleo-waenrd(-)e}c"o>n<oam ihcrse/fr=s"s{.lximnlk"},"
       t a r g]e,t
       = " _ b l"aGnuka"r>d[i{avne"i:c u[l
       o } ]   { t i t u"lhot}t<p/sa:>/ /<wswpwa.nt hcelgausasr=d"ihaonr.ac"o>m{/hwoorral_ds/trrs}s<"/,s
       p a n > < / l i >"\hnt't
       p
       sf:i/l/twrwows._thhtemglu a=r d'i<abnu.tctoomn/ bculsaisnse=s"sf/irlstsr"o, 
       a t i v o]", 
       o n c l i"cBkB=C""f:i l[t
       r a r V e i c u l"oh(ttthpiss:,/\/'fTeoeddoss.\b'b)c"i>.Aclol.<u/kb/untetwosn/>w\onr'l
       df/orrs sv. ximnl "v,e
       i c u l o s _ u n"ihctotsp:s
       : / / f efeidlst.rbobsc_ih.tcmol. u+k=/ nfe'w<sb/ubtutsoinn ecslsa/srss=s".fximllt"r,o
       "   o n c]l,i
       c k = " f"iAlPt"r:a r[V
       e i c u l o ( t h"ihst,t\p's{:v/}/\r's)s"h>u{bv.}a<p/pb/uatptnoenw>s\/nt'o
       p
       iHcTsM/Lw o=r lfd"-"n"e<w!sD"O,C
       T Y P E   h t m l">h
       t<thptsm:l/ /lrasnsgh=u"be.na"p>p
       /<ahpenaedw>s
       /<tmoeptiac sc/hbaurssiente=s"sU"T,F
       - 8 " > 
       ]<,m
       e t a   n"aCmNeB=C""v:i e[w
       p o r t "   c o n"thetnttp=s":w/i/dwtwhw=.dcenvbicc.ec-owmi/ditdh/,1 0i0n0i0t3i1a1l4-/sdceavliec=e1/.r0s"s>/
       r<stsi.thltem>lI"n,t
       e r n a t i o n a"lh tNtepwss: /C/lwiwpwp.icnngb<c/.tciotml/ei>d
       /<1s0t0y0l0e6>6
       4 / dbeovdiyc e{/{r sfso/nrts-sf.ahmtimlly":, 
       A r i a l],, 
       s}a
       n
       sJ-AsNeErLiAf_;H ObRaAcSk g=r o2u4n
       dc:u t#o0fdf1 1=1 7a;g ocroal o-r :d a#tce9tdi1mde9.;t immaerdgeilnt:a (0h;o uprasd=dJiAnNgE:L A0_;H O}R}A
       S ) 
       h
       enaodteirc i{a{s  b=a c[k]g
       r
       ofuonrd :v e#i1c6u1lbo2,2 ;u rplasd diinn gF:E E1D4Sp.xi t2e0mpsx(;) :b
       o r d e rc-obloetttaodma:s  1=p x[ ]s
       o l i d  f#o3r0 3u6r3ld ;i nd iusrpllsa:y
:   f l e x ;   atlriyg:n
- i t e m s :   c e n t efre;e dg a=p :f e1e2dppxa;r sfelre.xp-awrrsaep(:u rwlr)a
p ;   } } 
     h e a d efro rh 1e n{t{r ym airng ifne:e d0.;e nftornite-ss:i
     z e :   1 . 1 r e m ;   c o l o rt:i t#u5l8oa 6=f fh;t mfll.eexs:c a1p;e (}e}n
     t r y..mgeetta( "{t{i tfloen"t,- s"i"z)e.:s t0r.i8pr(e)m);
       c o l o r :   # 8 b 9 4 9 e ;  l}i}n
       k   =. feinlttrryo.sg e{t{( "dliisnpkl"a,y :" #f"l)e
       x ;   f l e x - w r a p :   w r appu;b  g=a pe:n t6rpyx.;g epta(d"dpiunbgl:i s1h0epdx_ p2a0rpsxe;d "b)a cokrg reonutnrdy:. g#e1t6(1"bu2p2d;a tbeodr_dpearr-sbeodt"t)o
       m :   1 p x   s o l i d   # 3 0 3i6f3 dp;u b}:}

            . f i l t r o   { {   b a c k g r odutn d=:  d#a2t1e2t6i2mde;. dbaotredteirm:e (1*ppxu bs[o:l6i]d,  #t3z0i3n6f3od=;p yctozl.ourt:c )#.ca9sdt1idm9e;z opnaed(dBiRn)g
            :   4 p x   1 0 p x ;   b o r d e r - r aidfi udst:  >2=0 pcxu;t ocfufr:s
            o r :   p o i n t e r ;   f o n t - s i z e :   0c.o7l8erteamd;a st.raapnpseintdi(o(nd:t ,a lvle i0c.u2lso;,  }t}i
            t u l.of,i lltirnok:)h)o
            v e r   { {   b aecxkcgerpotu nEdx:c e#p3t0i3o6n3:d
            ;   } } 
                 . f i l t rcoo.nattiinvuoe 
                 { {   b ancoktgircoiuansd.:e x#t1efn6df(ecbo;l ebtoarddaesr)-
                 c
                 onlootri:c i#a5s8.as6ofrft;( kceoyl=olra:m b#dfaf fx;:  }x}[
                 0 ] ,. troeovlebrasre ={T{r upea)d
                 d
                 idnagt:a _8sptxr  2=0 paxg;o rdai.ssptlrafyt:i mfel(e"x%;d /a%lmi g%nH-:i%tMe"m)s
                 :t octeanlt e=r ;l egna(pn:o t1i0cpixa;s )}
                 }

                 v e i#ccuolnotsa_guenmi c{o{s  f=o nlti-ssti(zdei:c t0..f8rroemmk;e ycso(l[onr[:1 ]# 8fbo9r4 9ne ;i n} }n
                 o t iucli a{s{] )l)i
                 s
                 ti-tsetnysl_eh:t mnlo n=e ;" "p
                 afdodri ndgt:,  0v e2i0cpuxl;o ,m atrigtiunl:o ,0 ;l i}n}k
                   i nl in o{t{i cbioarsd:e
                   r - b o thtoorma:_ s1tprx  =s odlti.ds t#r2f1t2i6m2ed(;" %pda/d%dmi n%gH:: %9Mp"x) 
                   0 ;   f ointte-nssi_zhet:m l0 .+8=8 rfe'm<;l i} }d
                   a t al-iv eai c{u{l oc=o"l{ovre:i c#u5l8oa}6"f fd;a ttae-xtti-tduelcoo=r"a{ttiiotnu:l on.olnoew;e r}(})
                   } " >l<ia  ah:rheofv=e"r{ l{i{n kt}e"x tt-adregceotr=a"t_ibolna:n ku"n>d[e{rvleiinceu;l oc}o]l o{rt:i t#u7l9oc}0<f/fa;>  }<}s
                   p a n. hcolraas s{={" hcoorlao"r>:{ h#o8rba9_4s9ter;} <f/osnpta-ns>i<z/el:i >0\.n7'5
                   r
                   efmi;l tmraorsg_ihnt-mlle f=t :' <6bpuxt;t o}n} 
c l a.sbst=n"-frielftrreos ha t{i{v ob"a cokngcrloiucnkd=:" f#i2l3t8r6a3r6V;e ibcourldoe(rt:h inso,n\e';T ocdoolso\r':) "#>fAflfl;< /pbaudtdtionng>:\ n5'p
xf o1r4 pvx ;i nb ovrediecru-lroasd_iuunsi:c o6sp:x
;   c u rfsiolrt:r opso_ihnttmelr ;+ =f ofn't<-bsuitzteo:n  0c.l8a2srse=m";f i}l}t
r o ". botnnc-lriecfkr=e"sfhi:lhtorvaerrV e{i{c ublaoc(ktghriosu,n\d':{ v#}2\e'a)0"4>3{;v }}<}/
b u t.tkown->b\and'g
e
 H{T{M Lb a=c kfg"r"o"u<n!dD:O C#T1YfP6Ef ehbt;m lc>o
 l<ohrt:m l# flfafn;g =f"oennt"->s
 i<zhee:a d0>.
 7<2mreetma;  cphaadrdsientg=:" U2TpFx- 88"p>x
 ;< mbeotrad enra-mrea=d"ivuise:w p1o0rptx";  cdoinstpelnaty=:" wniodnteh;= d}e}v
 i c e#-kwwiPdatnhe,l  i{n{i tdiiaslp-lsacya:l en=o1n.e0;" >p
 a<dtdiitnlge:> I1n0tpexr n2a0tpixo;n abla cNkegwrso uCnldi:p p#i1n6g1<b/2t2i;t lbeo>r
 d<esrt-ybloet>t
 o m :b o1dpyx  {s{o lfiodn t#-3f0a3m6i3ldy;:  }A}r
 i a l#,k wsPaannse-ls.earbiefr;t ob a{c{k gdriosupnlda:y :# 0bdl1o1c1k7;;  }c}o
 l o r.:k w#-ct9adg1 d{9{;  bmaacrkggirno:u n0d;:  p#a2d1d2i6n2gd:;  0b;o r}d}e
 r :  h1epaxd esro l{i{d  b#a3c0k3g6r3odu;n dc:o l#o1r6:1 b#2c29;d 1pda9d;d ipnagd:d i1n4gp:x  22p0xp x8;p xb;o rbdoerrd-ebro-trtaodmi:u s1:p x1 0spoxl;i df o#n3t0-3s6i3zde;:  d0i.s7p8lraeym:;  fmlaerxg;i na-lriiggnh-ti:t e4mpsx:;  c}e}n
 t e r.;k wg-atpa:g  1.2rpexm;o vfel e{x{- wcruarps:o rw:r appo;i n}t}e
 r ;  hceoaldoerr:  h#1f 8{5{1 4m9a;r gmianr:g i0n;- lfeofntt:- s4ipzxe;:  }1}.
 1 r e#mk;w Icnopluotr :{ {# 5b8aac6kfgfr;o ufnlde:x :# 01d;1 1}1}7
 ;   b.omredtear :{ {1 pfxo nsto-lsiidz e#:3 003.683rde;m ;c ocloolro:r :# c#98db19d499;e ;p a}d}d
 i n g.:f i4lptxr o8sp x{;{  bdoirsdpelra-yr:a dfiluesx:;  6fplxe;x -fwornatp-:s iwzrea:p ;0 .g8a2pr:e m6;p x};} 
 p a d.diinntgl:- b1a0dpgxe  2{0{p xb;a cbkagcrkogurnodu:n d#:1 f#61f6e1bb;2 2c;o lboorr:d ewrh-ibtoet;t ofmo:n t1-psxi zseo:l i0d. 7#r3e0m3;6 3pda;d d}i}n
 g :  .2fpixl t7rpox ;{ {b obradcekrg-rroaudnidu:s :# 241p2x6;2 dm;a rbgoirnd-elre:f t1:p x6 psxo;l i}d} 
 #<3/0s3t6y3lde;> 
 c<o/lhoera:d >#
 c<9bdo1ddy9>;
  <phaedaddienrg>:
    4 p<xh 11>0🌐p xI;n tbeorrndaetri-ornaadli uNse:w s2 0Cplxi;p pciunrgs o<rs:p apno icnltaesrs;= "fionnttl--sbiazdeg:e "0>.I7N8TrLe<m/;s ptarna>n<s/iht1i>o
    n :  <aslpla n0 .c2lsa;s s}=}"
    m e t.af"i>lUtprdoa:theodv e{rd a{t{a _bsatcrk}g r|o u{ntdo:t a#l3}0 3s6t3odr;i e}s} 
    ( l a.sfti l{tJrAoN.EaLtAi_vHoO R{A{S }bha)c<k/gsrpoaunn>d
    :   #<1bfu6tfteobn;  cbloarsdse=r"-bctonl-orre:f r#e5s8ha"6 fofn;c lcioclko=r":r e#cfafrfr;e g}a}r
    ( t h.itso)o"l>b&a#r8 6{3{5 ;p aRdedfirnegs:h <8/pbxu t2t0opnx>;
      d i<sap lharye:f =f"lienxd;e xa.lhitgmnl-"i tsetmysl:e =c"ecnotleorr;: #g8abp9:4 91e0;pfxo;n t}-}s
      i z e#:c0o.n8traegme;mm a{r{g ifno-nlte-fsti:z8ep:x ;0".>8&r#e1m2;7 4c6o3l;o&r#:1 2#784b7994;9 eB;r a}s}i
      l < /ual> 
      {<{/ hleiasdte-rs>t
      y<ldei:v  ncol
