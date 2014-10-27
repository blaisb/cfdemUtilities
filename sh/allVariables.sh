
var1=theta0
var2=thetaf
var3=PhiAngle
var4=radiusParticle

var5=InitialVelocityX
var6=InitialVelocityY
var7=FinalVelocityX
var8=FinalVelocityY

grep $var1 log | cut -c 18- > out$var1
grep $var2 log | cut -c 18- > out$var2
grep $var3 log | cut -c 18- > out$var3
grep $var4 log | cut -c 18- > out$var4

grep $var5 log | cut -c 18- > out$var5
grep $var6 log | cut -c 18- > out$var6
grep $var7 log | cut -c 18- > out$var7
grep $var8 log | cut -c 18- > out$var8
