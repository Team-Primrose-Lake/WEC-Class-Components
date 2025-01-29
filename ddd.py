import matlab.engine

# Start MATLAB engine
eng = matlab.engine.start_matlab()

# Query MATLAB version
matlab_version = eng.version()
print(f"MATLAB Version: {matlab_version}")

# Close MATLAB engine
eng.quit()
