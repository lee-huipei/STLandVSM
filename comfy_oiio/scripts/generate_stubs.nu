const root = (path self | path dirname | path dirname)

export def main [] {
  cd $root

  stubgen --include-docstrings -p OpenImageIO -o typings  --include-private
  let stub = "typings/OpenImageIO/OpenImageIO.pyi"
  open $stub | str replace -a -r "object at 0x[0-9a-fA-F]+" "object" | save -f $stub

}
