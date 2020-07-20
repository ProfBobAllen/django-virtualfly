                var flyNumber = 0;
                function updateFlies()
                {
                        flyNumber++;
                        var fliesData = document.getElementsByName("female");
                        var theFlies = "" + flyNumber + "\nfemale: ";
                        for (i=0; i<fliesData.length; i++)
                                if (fliesData[i].checked)
                                {
                                        theFlies += fliesData[i].value + " ";
                                        fliesData[i].checked = false;
                                }
                        fliesData = document.getElementsByName("male");
                        theFlies += "\nmale: ";
                        for (i=0; i<fliesData.length; i++)
                                if (fliesData[i].checked)
                                {
                                        theFlies += fliesData[i].value + " ";
                                        fliesData[i].checked = false;
                                }
                        document.getElementById("GenFlies").innerHTML += theFlies + "\n";
                }
