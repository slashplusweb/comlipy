class Comlipy < Formula
  desc "comlipy by slashplus - lint commit messages with python"
  homepage "https://gitlab.com/slashplus-build/comlipy/"
  url "https://files.pythonhosted.org/packages/fa/21/236be034d8498d264ba96ebc386dde29fbd2bedcb1d58277dbcc0d470e6c/comlipy-1.2.1.tar.gz"
  sha256 "cc5253dd55f002f958cfab56dec7af714d42b8cfb0171a591157b1440c4d6878"
  head "https://gitlab.com/slashplus-build/comlipy.git", :using => :git
  version "1.2.1"
  depends_on "python"

  include Language::Python::Virtualenv

  # See: https://github.com/Homebrew/brew/blob/master/docs/Python-for-Formula-Authors.md
  # Use 'poet -r $package' (https://pypi.python.org/pypi/homebrew-pypi-poet) to generate
  resource "click" do
    url "https://files.pythonhosted.org/packages/f8/5c/f60e9d8a1e77005f664b76ff8aeaee5bc05d0a91798afd7f53fc998dbc47/Click-7.0.tar.gz"
    sha256 "5b94b49521f6456670fdb30cd82a4eca9412788a93fa6dd6df72c94d5a8ff2d7"
  end

  resource "PyYAML" do
    url "https://files.pythonhosted.org/packages/3d/d9/ea9816aea31beeadccd03f1f8b625ecf8f645bd66744484d162d84803ce5/PyYAML-5.3.tar.gz"
    sha256 "e9f45bd5b92c7974e59bcd2dcc8631a6b6cc380a904725fce7bc08872e691615"
  end

  def install
    virtualenv_install_with_resources
  end

end
