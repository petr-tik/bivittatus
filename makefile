clean:
	rm -rf build/
	rm -f *.so

ext:
	chmod +x build.py
	./build.py build_ext --inplace

test:
	python3 -m pytest test.py

bench:	clean ext test
	free && sync && sudo sh -c "echo 3 > /proc/sys/vm/drop_caches" && free
	python3 benchmark.py
