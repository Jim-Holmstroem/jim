clean:
	find -name *.pyc | xargs -I{} bash -c 'function delete () { rm -f $$1 && echo "Deleted $$1"; } && delete {}'
