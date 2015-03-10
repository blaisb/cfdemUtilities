for file in foo[0-9]*.dump; do
  # strip the prefix ("foo") off the file name
  postfile=${file#foo}
  # strip the postfix (".png") off the file name
  number=${postfile%.dump}
  i=$number
  # copy to a new name in a new folder
  cp ${file} ./$(printf foo%09d.dump $i)
done
