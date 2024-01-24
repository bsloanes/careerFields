from readPDFs import *
from downloadPDFs import *

def main():
    # Install necessary packages
    loadPackages('getPDFsPkgs.txt')
    #Gets pdfs from one pg
    #downloadPDFfiles("https://www.e-publishing.af.mil/Product-Index/#/?view=search&keyword=CFETP&isObsolete=false&modID=449&tabID=131")
    
    #Gets pdfs from CFETP folder
    downloadNscroll("https://www.e-publishing.af.mil/Product-Index/#/?view=pubs&orgID=10141&catID=1&series=86&modID=449&tabID=131")
    
    #Gets pdfs from CFETP search
    #downloadNscroll("https://www.e-publishing.af.mil/Product-Index/#/?view=search&keyword=CFETP&isObsolete=false&modID=449&tabID=131")
    
if __name__ == "__main__":
    main()