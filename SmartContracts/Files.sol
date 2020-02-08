pragma solidity ^0.5.0;

contract Files
{
    uint public fileCount = 0;

    struct File
    {
        uint id;
        string filename;
        string filepath;
        bool verified;
    }

    mapping(uint => File) files;

    function createFileEntry(string memory _filename,string memory _filepath) public
    {
        fileCount++;
        files[fileCount] = File(fileCount,_filename,_filepath,false);
    }
    
    function getLastEntry() view public returns (string memory)
    {
        string memory fname = files[fileCount].filename;
        return fname;
    }
}