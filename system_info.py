import platform
import os

print("==========================================")
print("       SYSTEM AUTOMATION INSPECTOR        ")
print("==========================================")

# Query Operating System and Hardware details
print(f"OS Name:       {platform.system()}")
print(f"OS Release:    {platform.release()}")
print(f"Architecture:  {platform.machine()}")
print(f"Hostname:      {platform.node()}")

# Query Python Runtime details
print(f"Python Ver:    {platform.python_version()}")

# Check current active directory
print(f"Working Dir:   {os.getcwd()}")
print("==========================================")
