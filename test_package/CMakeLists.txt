cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(quickfix REQUIRED)

add_executable(example
	example.cpp
	Application.cpp
)

if(HAVE_SSL)
	target_compile_definitions(example
		PRIVATE
			HAVE_SSL
	)
endif()

target_link_libraries(example quickfix::quickfix)
