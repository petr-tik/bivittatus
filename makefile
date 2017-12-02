



clean:
	rm -rf build/
	rm -f *.so

ext:
	chmod +x build.py
	./build.py build_ext --inplace

test:
	python3 -m pytest test.py
