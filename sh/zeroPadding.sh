prefix=$1

for file in $prefix[0-9]*.dump; do
  # strip the prefix ("foo") off the file name
  postfile=${file#$prefix}
  # strip the postfix (".png") off the file name
  number=${postfile%.dump}
  i=$number
  # copy to a new name in a new folder
  cp ${file} ./$2/$(printf mixerCoupled_%09d.dump $i)
done

