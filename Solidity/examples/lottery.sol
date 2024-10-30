// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Lottery {
    address public manager;
    address payable[] public players;

    constructor() {
        manager = msg.sender;
    }

    function alreadyEntered() private view returns (bool) {
        for (uint i = 0; i < players.length; i++) {
            if (players[i] == msg.sender) {
                return true;
            }
        }
        return false;
    }

    function enter() public payable {
        require(msg.sender != manager, "Manager cannot enter");
        require(!alreadyEntered(), "Player already entered");
        require(msg.value >= 1 ether, "Minimum amount must be paid");
        players.push(payable(msg.sender));
    }

    function random() private view returns (uint) {
        return uint(keccak256(abi.encodePacked(block.prevrandao, block.timestamp, players)));
    }

    function pickWinner() public {
        require(msg.sender == manager, "Only Manager can pick the winner");
        require(players.length > 0, "No players in the lottery");
        uint index = random() % players.length;
        players[index].transfer(address(this).balance);
        players = new address payable[](0);
    }

    function getPlayers() public view returns (address payable[] memory) {
        return players;
    }
}