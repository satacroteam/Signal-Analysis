import matplotlib.pyplot as plt

from pyAudioAnalysis import audioBasicIO, audioFeatureExtraction

# Import data
[Fs, x] = audioBasicIO.readAudioFile("data/AS003-a-tenu-9010H42.WAV")
F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
plt.subplot(2, 1, 1)
plt.plot(F[0][0, :])
plt.xlabel('Frame no')
plt.ylabel('ZCR')

plt.subplot(2, 1, 2)
plt.plot(F[0][1, :])
plt.xlabel('Frame no')
plt.ylabel('Energy')

plt.show()
