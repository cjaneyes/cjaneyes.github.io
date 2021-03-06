/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 1.3.36
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

namespace Lemur {

using System;
using System.Runtime.InteropServices;

public class IndexManager : IDisposable {
  private HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal IndexManager(IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new HandleRef(this, cPtr);
  }

  internal static HandleRef getCPtr(IndexManager obj) {
    return (obj == null) ? new HandleRef(null, IntPtr.Zero) : obj.swigCPtr;
  }

  ~IndexManager() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if(swigCPtr.Handle != IntPtr.Zero && swigCMemOwn) {
        swigCMemOwn = false;
        lemur_csharpPINVOKE.delete_IndexManager(swigCPtr);
      }
      swigCPtr = new HandleRef(null, IntPtr.Zero);
      GC.SuppressFinalize(this);
    }
  }

  public static Index openIndex(string indexTOCFile) {
    IntPtr cPtr = lemur_csharpPINVOKE.IndexManager_openIndex(indexTOCFile);
    Index ret = (cPtr == IntPtr.Zero) ? null : new Index(cPtr, false);
    if (lemur_csharpPINVOKE.SWIGPendingException.Pending) throw lemur_csharpPINVOKE.SWIGPendingException.Retrieve();
    return ret;
  }

  public IndexManager() : this(lemur_csharpPINVOKE.new_IndexManager(), true) {
  }

}

}
