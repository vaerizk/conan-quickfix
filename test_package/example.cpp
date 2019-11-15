/****************************************************************************
** Copyright (c) 2001-2018 Oren Miller
**
** This product includes software developed by
** quickfixengine.org (http://www.quickfixengine.org/).
**
****************************************************************************/

#ifdef _MSC_VER
#pragma warning( disable : 4503 4355 4786 )
#else
#include "config.h"
#endif

#include "quickfix/FileStore.h"
#include "quickfix/SocketInitiator.h"
#ifdef HAVE_SSL
#include "quickfix/ThreadedSSLSocketInitiator.h"
#include "quickfix/SSLSocketInitiator.h"
#endif
#include "quickfix/SessionSettings.h"
#include "quickfix/Log.h"
#include "Application.h"
#include <string>
#include <iostream>
#include <fstream>

int main( int argc, char** argv )
{
	std::string file = "tradeclient.cfg";
	std::cout << "Used: " << file << "\n";

#ifdef HAVE_SSL
	std::string isSSL = "SSL";
#endif

	FIX::Initiator * initiator = 0;
	try
	{
		FIX::SessionSettings settings( file );

		Application application;
		FIX::FileStoreFactory storeFactory( settings );
		FIX::ScreenLogFactory logFactory( settings );
#ifdef HAVE_SSL
		if (isSSL.compare("SSL") == 0) {
			initiator = new FIX::ThreadedSSLSocketInitiator ( application, storeFactory, settings, logFactory );
			std::cout << "ThreadedSSLSocketInitiator created\n";
		}
		else if (isSSL.compare("SSL-ST") == 0) {
			initiator = new FIX::SSLSocketInitiator ( application, storeFactory, settings, logFactory );
			std::cout << "SSLSocketInitiator created\n";
		}
		else
#endif
		{
			initiator = new FIX::SocketInitiator( application, storeFactory, settings, logFactory );
			std::cout << "SocketInitiator created\n";
		}

		delete initiator;

		std::cout << "Package test completed";

		return 0;
	}
	catch ( std::exception & e )
	{
		std::cout << e.what();
		delete initiator;
		return 1;
	}
}
