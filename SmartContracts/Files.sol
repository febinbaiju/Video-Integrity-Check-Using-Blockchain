pragma solidity ^0.5.0;

contract Files
{
    uint public fileCount = 0;

    struct File
    {
        uint id;
        string filename;
        string filepath;
        string key;
        string enckey;
    }

    mapping(uint => File) files;

    function createFileEntry(string memory _filename,string memory _filepath,string memory _filehash) public
    {
        fileCount++;
        files[fileCount] = File(fileCount,_filename,_filepath,_filehash);
    }
    
    function getTotalCount() view public returns (uint)
    {
        return fileCount;
    }
    
    
      function getLastEntry() view public returns (string memory) {
                    string memory fname = files[fileCount].filename;
                    string memory fhash = files[fileCount].filehash;
                    string memory filepath = files[fileCount].filepath;
                    return string(fname);
                     ///return string(abi.encodePacked(fname, filepath,fhash));
                  }
  
}