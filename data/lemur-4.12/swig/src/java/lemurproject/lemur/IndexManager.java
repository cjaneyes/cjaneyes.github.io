/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 1.3.36
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package lemurproject.lemur;

public class IndexManager {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  protected IndexManager(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(IndexManager obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  public synchronized void delete() {
    if(swigCPtr != 0 && swigCMemOwn) {
      swigCMemOwn = false;
      throw new UnsupportedOperationException("C++ destructor does not have public access");
    }
    swigCPtr = 0;
  }

  
/**
An utility function to open an index, automatically recognizing the indexer based on file extension. 
@param indexTOCFile the name of the index table of contents file, or base
repository directory for an indri repository.
@return reference to the open Index.
@throws Exception if the index fails to open.
*/
public static Index openIndex(String indexTOCFile) throws java.lang.Exception {
    long cPtr = lemurJNI.IndexManager_openIndex(indexTOCFile);
    return (cPtr == 0) ? null : new Index(cPtr, true);
  }

}