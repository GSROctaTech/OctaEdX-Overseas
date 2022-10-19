from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtCore import Qt, QUrl, QSize, QPoint, QRect
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QMessageBox, QVBoxLayout,
                             QWidget, QShortcut, QMenu, QToolTip, QPushButton)
from distutils.spawn import find_executable


class VideoPlayer(QWidget):
    def __init__(self):
        super(VideoPlayer, self).__init__()

        self.setAttribute(Qt.WA_NoSystemBackground, True)

        self.volume = 95
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.StreamPlayback)
        self.mediaPlayer.volumeChanged.connect(self.setVolume)
        self.mediaPlayer.setVolume(95)
        self.mediaPlayer.metaDataChanged.connect(self.metaDataChanged)

        self.videoWidget = QVideoWidget(self)
        self.videoWidget.setAspectRatioMode(0)
        #        self.videoWidget.setToolTip("Info")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.videoWidget)

        self.setLayout(layout)

        self.myinfo = "TV-Livestream\n©2016\nAxel Schneider\n\nMouse Wheel = Zoom\nUP = Volume Up\nDOWN = Volume Down\n"

        self.widescreen = True
        self.fullscreen = False

        self.rect = QRect()

        #### shortcuts ####
        self.shortcut = QShortcut(QKeySequence("q"), self)
        self.shortcut.activated.connect(self.handleQuit)
        self.shortcut = QShortcut(QKeySequence(" "), self)
        self.shortcut.activated.connect(self.play)
        self.shortcut = QShortcut(QKeySequence("f"), self)
        self.shortcut.activated.connect(self.handleFullscreen)
        self.shortcut = QShortcut(QKeySequence("i"), self)
        self.shortcut.activated.connect(self.handleAbout)
        self.shortcut = QShortcut(QKeySequence(Qt.Key_Up), self)
        self.shortcut.activated.connect(self.volumeUp)
        self.shortcut = QShortcut(QKeySequence(Qt.Key_Down), self)
        self.shortcut.activated.connect(self.volumeDown)
        self.shortcut = QShortcut(QKeySequence("u"), self)
        self.shortcut.activated.connect(self.playURL)
        self.shortcut = QShortcut(QKeySequence("m"), self)
        self.shortcut.activated.connect(self.handleMute)

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.error.connect(self.handleError)
        print("TV Livestream started")
        self.handleARD640()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            self.handleARD640()
        elif e.key() == Qt.Key_2:
            self.handleZDF640()
        elif e.key() == Qt.Key_3:
            self.handleMDR640()
        elif e.key() == Qt.Key_4:
            self.handlePhoenix()
        elif e.key() == Qt.Key_5:
            self.handleRBB640()
        elif e.key() == Qt.Key_6:
            self.handleBR640()
        elif e.key() == Qt.Key_7:
            self.handleHR640()
        elif e.key() == Qt.Key_8:
            self.handleARTE()
        elif e.key() == Qt.Key_9:
            self.handleONE()
        else:
            e.accept()

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        print("Error: " + self.mediaPlayer.errorString())

    def handleQuit(self):
        self.mediaPlayer.stop()
        print("Goodbye ...")
        app.quit()

    def contextMenuRequested(self, point):
        menu = QMenu()
        actionURL = menu.addAction("playURL (u)")
        actionURL.triggered.connect(self.playURL)
        actionARD = menu.addAction("ARD")
        actionZDF = menu.addAction("ZDF")
        actionPhoenix = menu.addAction("Phoenix")
        actionMDR = menu.addAction("MDR")
        actionHR = menu.addAction("HR")
        actionRBB = menu.addAction("RBB")
        actionBR = menu.addAction("BR")
        actionSR = menu.addAction("SR")
        actionNDR = menu.addAction("NDR")
        actionWDR = menu.addAction("WDR")
        actionARTE = menu.addAction("ARTE")
        actionNeo = menu.addAction("ZDF Neo")
        actionZDFInfo = menu.addAction("ZDF Info")
        actionONE = menu.addAction("ONE")
        actionSep = menu.addSeparator()
        actionORF1 = menu.addAction("ORF 1")
        actionORF2 = menu.addAction("ORF 2")
        actionORF3 = menu.addAction("ORF 3")
        menu.addSeparator()
        actionSkySportNews = menu.addAction("Sky Sport News")
        actionSport1 = menu.addAction("Sport1")
        menu.addSeparator()
        actionNTV = menu.addAction("ntv")
        actionSep = menu.addSeparator()
        menu640 = menu.addMenu("Resolution 640")
        actionARD_640 = menu640.addAction("ARD")
        actionZDF_640 = menu640.addAction("ZDF")
        actionPhoenix640 = menu640.addAction("Phoenix")
        actionMDR_640 = menu640.addAction("MDR")
        actionHR_640 = menu640.addAction("HR")
        actionRBB_640 = menu640.addAction("RBB")
        actionBR_640 = menu640.addAction("BR")
        actionNeo640 = menu640.addAction("Neo")
        actionInfo640 = menu640.addAction("Info")
        action3Sat640 = menu640.addAction("3Sat")
        actionT24_640 = menu640.addAction("Tagesschau 24")
        actionZDFheute = menu640.addAction("ZDF heute")

        actionsep2 = menu.addSeparator()
        actionFull = menu.addAction("Fullscreen (f)")
        action169 = menu.addAction("16 : 9")
        action43 = menu.addAction("4 : 3")
        actionSep = menu.addSeparator()
        actionInfo = menu.addAction("Info (i)")
        action5 = menu.addSeparator()
        actionMute = menu.addAction("Mute (m)")
        action6 = menu.addSeparator()
        actionQuit = menu.addAction("Exit (q)")

        actionMute.triggered.connect(self.handleMute)
        actionQuit.triggered.connect(self.handleQuit)
        actionFull.triggered.connect(self.handleFullscreen)
        actionInfo.triggered.connect(self.handleAbout)

        actionARD.triggered.connect(self.handleARD)
        actionONE.triggered.connect(self.handleONE)
        actionZDF.triggered.connect(self.handleZDF)
        actionPhoenix.triggered.connect(self.handlePhoenix)
        actionPhoenix640.triggered.connect(self.handlePhoenix640)
        actionMDR.triggered.connect(self.handleMDR)
        actionZDFInfo.triggered.connect(self.handleZDFInfo)
        actionHR.triggered.connect(self.handleHR)
        actionARTE.triggered.connect(self.handleARTE)
        actionRBB.triggered.connect(self.handleRBB)
        actionBR.triggered.connect(self.handleBR)
        actionSR.triggered.connect(self.handleSR)
        actionNDR.triggered.connect(self.handleNDR)
        actionWDR.triggered.connect(self.handleWDR)
        actionNeo.triggered.connect(self.handleNeo)
        actionORF1.triggered.connect(self.handleORF1)
        actionORF2.triggered.connect(self.handleORF2)
        actionORF3.triggered.connect(self.handleORF3)
        actionNTV.triggered.connect(self.handleNTV)
        actionSkySportNews.triggered.connect(self.handleSkySportNews)
        actionARD_640.triggered.connect(self.handleARD640)
        actionZDF_640.triggered.connect(self.handleZDF640)
        actionMDR_640.triggered.connect(self.handleMDR640)
        actionHR_640.triggered.connect(self.handleHR640)
        actionRBB_640.triggered.connect(self.handleRBB640)
        actionBR_640.triggered.connect(self.handleBR640)
        actionNeo640.triggered.connect(self.handleNeo640)
        actionInfo640.triggered.connect(self.handleInfo640)
        action3Sat640.triggered.connect(self.handle3SAT)
        actionT24_640.triggered.connect(self.handleT24)
        actionZDFheute.triggered.connect(self.handleZDFheute)

        action169.triggered.connect(self.screen169)
        action43.triggered.connect(self.screen43)
        actionSport1.triggered.connect(self.handleSport1)

        menu.exec_(self.mapToGlobal(point))

    def wheelEvent(self, event):
        mwidth = self.frameGeometry().width()
        mheight = self.frameGeometry().height()
        mleft = self.frameGeometry().left()
        mtop = self.frameGeometry().top()
        mscale = event.angleDelta().y() / 5
        if self.widescreen == True:
            self.setGeometry(mleft, mtop, mwidth + mscale, (mwidth + mscale) / 1.778)
        else:
            self.setGeometry(mleft, mtop, mwidth + mscale, (mwidth + mscale) / 1.33)

    def handleMute(self):
        if not self.mediaPlayer.isMuted():
            self.mediaPlayer.setMuted(True)
        else:
            self.mediaPlayer.setMuted(False)

    def handleFullscreen(self):
        #        if self.windowState() & QtCore.Qt.WindowFullScreen:
        if self.fullscreen == True:
            self.fullscreen = False
            print("no Fullscreen")
        else:
            self.rect = self.geometry()
            screen = QApplication.primaryScreen()
            screenGeometry = QRect(screen.geometry())
            self.setGeometry(0, 30, screenGeometry.width(), screenGeometry.width() / 1.778)
            self.fullscreen = True
            print("Fullscreen entered")
        if self.fullscreen == False:
            self.setGeometry(self.rect)

    def handleAbout(self):
        msg = QMessageBox.about(self, "QT5 Player", self.myinfo)

    def volumeUp(self):
        self.mediaPlayer.setVolume(self.mediaPlayer.volume() + 10)
        print("Volume: " + str(self.mediaPlayer.volume()))

    def setVolume(self):
        self.volume = self.mediaPlayer.volume()

    def volumeDown(self):
        self.mediaPlayer.setVolume(self.mediaPlayer.volume() - 10)
        print("Volume: " + str(self.mediaPlayer.volume()))

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() \
                      - QPoint(self.frameGeometry().width() / 2, \
                               self.frameGeometry().height() / 2))
            event.accept()

    def screen169(self):
        self.widescreen = True
        mwidth = self.frameGeometry().width()
        mheight = self.frameGeometry().height()
        mleft = self.frameGeometry().left()
        mtop = self.frameGeometry().top()
        mratio = 1.778
        self.setGeometry(mleft, mtop, mwidth, mwidth / mratio)

    def screen43(self):
        self.widescreen = False
        mwidth = self.frameGeometry().width()
        mheight = self.frameGeometry().height()
        mleft = self.frameGeometry().left()
        mtop = self.frameGeometry().top()
        mratio = 1.33
        self.setGeometry(mleft, mtop, mwidth, mwidth / mratio)

    ############################### TV ################################

    def playURL(self):
        clip = QApplication.clipboard()
        myurl = clip.text()
        self.mediaPlayer.setMedia(QMediaContent(QUrl(myurl)))
        self.mediaPlayer.play()

    def metaDataChanged(self):
        if self.mediaPlayer.isMetaDataAvailable():
            trackInfo = self.mediaPlayer.metaData("Title")
            if not trackInfo == None:
                print(trackInfo)
        else:
            print("playing")

    def findYouTube(self):
        ytdl = find_executable('youtube-dl')
        if ytdl == None:
            return False
        else:
            print("found youtube-dl")
            return True

    def handleSport1(self):
        if self.findYouTube() == True:
            import subprocess
            cmd = "youtube-dl -g https://tv.sport1.de/sport1/"
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
            (link, err) = proc.communicate()
            print(link)
            myurl = str(link).partition('\n')[0]  # .partition("b'")[2].replace("\n", "")
            if not myurl == "":
                self.playtv(myurl)
            else:
                msg = QMessageBox.about(self, "TVLive", "URL not found")
        else:
            msg = QMessageBox.about(self, "TVLive", "youtube-dl not found")

    def handleZDFheute(self):
        myurl = "https://zdf0102-lh.akamaihd.net/i/none01_v1@392849/index_776_av-p.m3u8?sd=10&rebase=on"
        self.playtv(myurl)

    def handleNTV(self):
        myurl = "https://ntvlivehls-lh.akamaihd.net/i/ntvlivehls_1@409250/index_1500_av-p.m3u8"
        self.playtv(myurl)

    def handleSkySportNews(self):
        myurl = "https://eventhlshttps-i.akamaihd.net/hls/live/263645/ssn-hd-https/indexvideo-3400.m3u8"
        self.playtv(myurl)

    def handleSkySportNews640(self):
        myurl = "https://eventhlshttps-i.akamaihd.net/hls/live/263645/ssn-hd-https/indexvideo-3400.m3u8"
        self.playtv(myurl)

    def handleT24(self):
        myurl = "http://tagesschau-lh.akamaihd.net/i/tagesschau_1@119231/index_1152_av-p.m3u8"
        self.playtv(myurl)

    def handle3SAT(self):
        myurl = "http://zdf0910-lh.akamaihd.net/i/dach10_v1@392872/index_750_av-p.m3u8"
        self.playtv(myurl)

    def handlePhoenix(self):
        myurl = "http://zdf0910-lh.akamaihd.net/i/de09_v1@392871/master.m3u8"
        self.playtv(myurl)

    def handlePhoenix640(self):
        myurl = "http://zdf0910-lh.akamaihd.net/i/de09_v1@392871/index_750_av-p.m3u8"
        self.playtv(myurl)

    def handleONE(self):
        myurl = "http://onelivestream-lh.akamaihd.net/i/one_livestream@568814/index_5_av-p.m3u8"
        self.playtv(myurl)

    def handleARD(self):
        myurl = "http://daserstehdde-lh.akamaihd.net/i/daserstehd_de@629196/master.m3u8"
        self.playtv(myurl)

    def handleZDF(self):
        myurl = "http://zdf1314-lh.akamaihd.net/i/de14_v1@392878/master.m3u8"
        self.playtv(myurl)

    def handleARD640(self):
        myurl = "http://daserstehdde-lh.akamaihd.net/i/daserstehd_de@629196/index_1216_av-p.m3u8?sd=10&rebase=on"
        self.playtv(myurl)

    def handleZDF640(self):
        myurl = "http://zdf1314-lh.akamaihd.net/i/de14_v1@392878/index_776_av-b.m3u8"
        self.playtv(myurl)

    def handleMDR(self):
        myurl = "http://mdrthuhls-lh.akamaihd.net/i/livetvmdrthueringen_de@514027/master.m3u8"
        self.playtv(myurl)

    def handleMDR640(self):
        myurl = "http://mdrthuhls-lh.akamaihd.net/i/livetvmdrthueringen_de@514027/index_1216_av-b.m3u8?sd=10&rebase=on"
        self.playtv(myurl)

    def handleRBB(self):
        myurl = "http://rbblive-lh.akamaihd.net/i/rbb_berlin@144674/master.m3u8"
        self.playtv(myurl)

    def handleRBB640(self):
        myurl = "http://rbblive-lh.akamaihd.net/i/rbb_berlin@144674/index_5_av-p.m3u8"
        self.playtv(myurl)

    def handleHR(self):
        myurl = "http://live1_hr-lh.akamaihd.net/i/hr_fernsehen@75910/master.m3u8"
        self.playtv(myurl)

    def handleHR640(self):
        myurl = "http://live1_hr-lh.akamaihd.net/i/hr_fernsehen@75910/index_1024_av-p.m3u8"
        self.playtv(myurl)

    def handleBR(self):
        myurl = "http://livestreams.br.de/i/bfsnord_germany@119898/master.m3u8"
        self.playtv(myurl)

    def handleBR640(self):
        myurl = "http://livestreams.br.de/i/bfsnord_germany@119898/index_1216_av-p.m3u8"
        self.playtv(myurl)

    def handleSR(self):
        myurl = "http://livestream.sr-online.de/live.m3u8"
        self.playtv(myurl)

    def handleNDR(self):
        myurl = "https://ndrfs-lh.akamaihd.net/i/ndrfs_nds@430233/master.m3u8"
        self.playtv(myurl)

    def handleWDR(self):
        myurl = "http://wdrfsgeo-lh.akamaihd.net/i/wdrfs_geogeblockt@530016/master.m3u8"
        self.playtv(myurl)

    def handleZDFInfo(self):
        myurl = "http://zdf1112-lh.akamaihd.net/i/de12_v1@392882/master.m3u8"
        self.playtv(myurl)

    def handleInfo640(self):
        myurl = "http://zdf1112-lh.akamaihd.net/i/de12_v1@392882/index_776_av-p.m3u8"
        self.playtv(myurl)

    def handleNeo(self):
        myurl = "http://zdf1314-lh.akamaihd.net/i/de13_v1@392877/master.m3u8"
        self.playtv(myurl)

    def handleNeo640(self):
        myurl = "http://zdf1314-lh.akamaihd.net/i/de13_v1@392877/index_776_av-b.m3u8?sd=10&rebase=on"
        self.playtv(myurl)

    def handleMDRPlus(self):
        myurl = "http://liveevent1.mdr.de/i/livetvmdrevent1_ww@106904/index_1106_av-b.m3u8"  # ?sd=10&rebase=on
        self.playtv(myurl)

    def handleAlpha(self):
        myurl = "http://livestreams.br.de/i/bralpha_germany@119899/master.m3u8"
        self.playtv(myurl)

    def handleARTE(self):
        myurl = "http://artelive-lh.akamaihd.net/i/artelive_de@393591/master.m3u8"
        self.playtv(myurl)

    def handleORF1(self):
        myurl = "http://apasfiisl.apa.at/ipad/orf1_q4a/orf.sdp/playlist.m3u8"
        self.playtv(myurl)

    def handleORF2(self):
        myurl = "http://apasfiisl.apa.at/ipad/orf2_q4a/orf.sdp/playlist.m3u8"
        self.playtv(myurl)

    def handleORF3(self):
        myurl = "http://apasfiisl.apa.at/ipad/orf3_q4a/orf.sdp/playlist.m3u8"
        self.playtv(myurl)

    def playtv(self, myurl):
        try:
            self.mediaPlayer.setMedia(QMediaContent(QUrl(myurl)))
            self.mediaPlayer.play()
        except Exception as e:
            msg = QMessageBox.about(self, "QT5 Player", str(e))
            print('Error: ' + str(e))
            pass


############################### Ende TV ################################

if __name__ == '__main__':
    from sys import argv, exit

    app = QApplication(argv)

    player = VideoPlayer()
    player.setAcceptDrops(True)
    player.setWindowTitle("TV Livestream")
    player.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    player.setGeometry(0, 80, 400, 400)# / 1.778)
    screen = QApplication.primaryScreen()
    screenGeometry = QRect(screen.geometry())
    screensize = QPoint(screenGeometry.width(), screenGeometry.height())
    p = QPoint(player.mapToGlobal(QPoint(screensize)) -
               QPoint(player.size().width() + 2, player.size().height() + 2))
    player.move(p)

    screenGeometry = QApplication.desktop().availableGeometry()
    screenGeo = screenGeometry.bottomRight()
    player.move(screenGeo)
    player.setContextMenuPolicy(Qt.CustomContextMenu);
    player.customContextMenuRequested[QPoint].connect(player.contextMenuRequested)
    #    player.handleARD()
    player.show()
exit(app.exec_())