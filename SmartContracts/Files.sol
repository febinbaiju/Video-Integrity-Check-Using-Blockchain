pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

contract Files
{
    uint public fileCount = 0;
    string [] private keys;
    string [] private hashes;

    struct File
    {
        uint id;
        string filename;
        string filepath;
        string pubkey;
        string filehash;
    }

    mapping(uint => File) files;

      function addKey (string memory str) public {
    keys.push (str);
  }

        function addHash (string memory str) public {
    hashes.push (str);
  }


    function getKeys () public view returns (string [] memory) {
    return keys;
  }
    function getHashes () public view returns (string [] memory) {
    return hashes;
  }
    function createFileEntry(string memory _filename,string memory _filepath,string memory _pubkey,string memory _filehash) public
    {
        fileCount++;
        files[fileCount] = File(fileCount,_filename,_filepath,_pubkey,_filehash);
        addKeys();
        addHashes();
    }

    function getTotalCount() view public returns (uint)
    {
        return fileCount;
    }

    function addKeys() public
    {
        delete keys;

        for(uint i=0; i <= getTotalCount(); i++)
        {
            addKey(files[i].pubkey);
        }
    }

        function addHashes() public
    {
        delete hashes;

        for(uint i=0; i <= getTotalCount(); i++)
        {
            addHash(files[i].filehash);
        }
    }



      function getLastEntry() view public returns (string memory) {
                    string memory fname = files[fileCount].filename;
                    string memory filehash = files[fileCount].filehash;
                    string memory pubkey = files[fileCount].pubkey;
                    string memory filepath = files[fileCount].filepath;
                    ///return string(abi.encodePacked(pubkey," ",filehash));
                    return string(abi.encodePacked(fname, " ",filepath, " ",pubkey, " ",filehash));
                  }

}